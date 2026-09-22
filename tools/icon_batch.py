"""
One icon sheet, start to finish: generate (Azure) → check → cut → contact sheet for the owner to approve.

  python3 tools/icon_batch.py fantasy-rpg-casual C1          # one sheet
  python3 tools/icon_batch.py fantasy-rpg-casual --all       # every sheet in the style's ICON-SHEETS.md
  python3 tools/icon_batch.py fantasy-rpg-casual C1 --cut-only   # re-cut an already generated sheet

Reads <style>/kit/assets/ICON-SHEETS.md (a "## Sheet ID — title" heading, a `name name …` line, a ``` prompt).
Sheets whose ID starts with W are white glyphs on black (alpha from brightness, painted white);
C sheets are colour items generated with a real alpha channel (--transparent), cut on that alpha, colours kept.
(flood_bg / transparent_sheet stay for sheets that arrive painted on white, e.g. from another model.)

The check, before anything is cut: the background must be one field reaching every edge (a tiled sheet
fails), and each of the 9 cells must hold one drawing of a sane size. A failed sheet is regenerated, up to
3 tries; then it stops and says so. Nothing is drawn in code — a bad cell means regenerate, never fix by hand.

Output:  _staging/icons/<style>/<ID>.png            the raw sheet
         <style>/kit/assets/<name>.png               the cut icons (160x160, ink-normalised)
         _staging/icons/<style>/<ID>-contact.png     sheet + the cut icons on the kit's dark tile, 1x and 2x
Then run  python3 tools/icon_offsets.py <style>/kit/assets <style>/kit/assets/offsets.css  once for the set.
"""
import pathlib, re, subprocess, sys
from collections import deque
import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont

ROOT = pathlib.Path(__file__).resolve().parent.parent
style = sys.argv[1]; ASSETS = ROOT / style / 'kit' / 'assets'
STAGE = ROOT / '_staging' / 'icons' / style; STAGE.mkdir(parents=True, exist_ok=True)
md = '\n'.join(f.read_text() for f in sorted(ASSETS.glob('ICON-SHEETS*.md')))      # the base list + any extension files
SHEETS = {}
for m in re.finditer(r'## Sheet (\w+) — [^\n(]+(?:\((\d+)x(\d+), (\d+x\d+), (\d+)\))?[^\n]*\n\n`([^`]+)`\n\n```\n(.*?)```', md, re.S):
    sid, cols, rows, size, canvas, names, prompt = m.groups()
    SHEETS[sid] = dict(names=names.split(), prompt=prompt.strip(), cols=int(cols or 3), rows=int(rows or 3), size=size or '1024x1024', canvas=int(canvas or 160))
dupes = [n for n in {n for s in SHEETS.values() for n in s['names']} if sum(s['names'].count(n) for s in SHEETS.values()) > 1]
if dupes: sys.exit(f'the same icon name is on two sheets: {dupes}')
want = list(SHEETS) if '--all' in sys.argv else [a for a in sys.argv[2:] if not a.startswith('--')]
if '--skip-done' in sys.argv:
    want = [s for s in want if not all((ASSETS / f'{n}.png').exists() for n in SHEETS[s]['names'])]
if '--list' in sys.argv:
    print(f'{len(SHEETS)} sheets known, {len(want)} to do: {" ".join(want)}'); sys.exit()

def flood_bg(arr, tol=30):
    """background reachable from the image edge (colour sheets)"""
    h, w, _ = arr.shape
    bg = np.median(np.concatenate([arr[0], arr[-1], arr[:, 0], arr[:, -1]]), axis=0)
    close = np.abs(arr - bg).max(axis=2) <= tol
    out = np.zeros((h, w), bool); q = deque()
    for x in range(w):
        for y in (0, h - 1):
            if close[y, x] and not out[y, x]: out[y, x] = True; q.append((y, x))
    for y in range(h):
        for x in (0, w - 1):
            if close[y, x] and not out[y, x]: out[y, x] = True; q.append((y, x))
    while q:
        cy, cx = q.popleft()
        for ny, nx in ((cy+1, cx), (cy-1, cx), (cy, cx+1), (cy, cx-1)):
            if 0 <= ny < h and 0 <= nx < w and close[ny, nx] and not out[ny, nx]:
                out[ny, nx] = True; q.append((ny, nx))
    return out, bg

def check(sheet, white, cols=3, rows=3, count=9):
    im = Image.open(sheet).convert('RGB'); arr = np.asarray(im).astype(np.int16); h, w, _ = arr.shape
    if white:
        ink = arr.mean(axis=2) > 115; bgmask = ~ink
        edge_ok = (arr[0].mean() < 60) and (arr[-1].mean() < 60) and (arr[:, 0].mean() < 60) and (arr[:, -1].mean() < 60)
    else:                                                    # colour sheets carry their own alpha (--transparent)
        al = np.asarray(Image.open(sheet).convert('RGBA'))[..., 3]
        if (al < 10).mean() < .3: return 'no real alpha channel came back — the background was painted instead'
        ink = al > 40; bgmask = ~ink
        edge_ok = (al[0].mean() < 8) and (al[-1].mean() < 8) and (al[:, 0].mean() < 8) and (al[:, -1].mean() < 8)
    if not edge_ok: return 'the edge of the image is not the flat background colour'
    if bgmask.mean() < .35: return f'background is only {bgmask.mean():.0%} of the image — tiled or filled'
    ch, cw = h / rows, w / cols
    for r in range(rows):
        for c in range(cols):
            if r * cols + c >= count: continue                     # a short last sheet leaves its final cells empty
            cell = ink[int(r * ch):int((r + 1) * ch), int(c * cw):int((c + 1) * cw)]
            f = cell.mean()
            if f < .025: return f'cell {r + 1},{c + 1} is empty ({f:.1%} ink)'
            if f > .8: return f'cell {r + 1},{c + 1} is nearly full ({f:.0%} ink) — probably a tile'   # big pack art with its glow can reach 65%
            # something must reach the cell's middle third — a drawing centred in its ninth
            mid = cell[int(cell.shape[0] * .3):int(cell.shape[0] * .7), int(cell.shape[1] * .3):int(cell.shape[1] * .7)]
            if mid.mean() < .01: return f'cell {r + 1},{c + 1} has nothing in its middle'
    # gutters: a thin strip on each inner grid line should be (almost) all background
    for k in range(1, rows):
        if bgmask[int(k * ch) - 6:int(k * ch) + 6, :].mean() < .55: return f'drawings cross horizontal grid line {k}'
    for k in range(1, cols):
        if bgmask[:, int(k * cw) - 6:int(k * cw) + 6].mean() < .55: return f'drawings cross vertical grid line {k}'
    return None

def transparent_sheet(sheet, out):
    """colour sheet → same size, background removed, edge un-blended (no crop, so the grid stays true)"""
    im = Image.open(sheet).convert('RGB'); arr = np.asarray(im).astype(np.int16)
    bgmask, bg = flood_bg(arr)
    alpha = np.where(bgmask, 0.0, 1.0)
    ring = np.asarray(Image.fromarray((bgmask * 255).astype('uint8')).filter(ImageFilter.MaxFilter(5))) > 0
    ring &= ~bgmask
    lum = arr.mean(axis=2); bg_lum = float(bg.mean())
    est = np.clip((bg_lum - lum) / max(bg_lum, 1.0), 0, 1)
    alpha[ring] = np.maximum(est[ring], .12)
    rgb = arr.astype(np.float32); m = ring & (alpha > .02)
    for c in range(3):
        ch = rgb[..., c]; ch[m] = np.clip((ch[m] - (1 - alpha[m]) * bg[c]) / alpha[m], 0, 255); rgb[..., c] = ch
    Image.fromarray(np.dstack([rgb.astype('uint8'), (alpha * 255).astype('uint8')]), 'RGBA').save(out)

def contact(sid, sheet, names, out):
    tile = (42, 36, 56); W_ = 1180; H_ = 560 if len(names) <= 10 else 760
    im = Image.new('RGB', (W_, H_), (24, 20, 32)); d = ImageDraw.Draw(im)
    s = Image.open(sheet).convert('RGBA').resize((520, 520)); back = Image.new('RGBA', s.size, (60, 52, 78, 255)); back.alpha_composite(s); im.paste(back.convert('RGB'), (20, 20))
    try: font = ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial.ttf', 13)
    except Exception: font = ImageFont.load_default()
    d.text((560, 20), f'{sid}: cut icons on the kit tile — 1x (64px) and 2x (128px)', fill=(220, 220, 235), font=font)
    for i, n in enumerate(names):
        p = ASSETS / f'{n}.png'
        if not p.exists(): continue
        ic = Image.open(p).convert('RGBA')
        for size, x0, y0 in ((64, 560 + (i % 9) * 66, 50), (128, 560 + (i % 5) * 122, 150 + (i // 5) * 190)):
            d.rounded_rectangle((x0, y0, x0 + size + 4, y0 + size + 4), 10, fill=tile)
            g = ic.resize((size, size), Image.LANCZOS); im.paste(g, (x0 + 2, y0 + 2), g)
            if size == 128: d.text((x0, y0 + size + 8), n, fill=(180, 180, 200), font=font)
    im.save(out)

failed = []
for sid in want:
    S = SHEETS[sid]; names, prompt = S['names'], S['prompt']; white = sid[0] in 'WG'
    sheet = STAGE / f'{sid}.png'; (STAGE / f'{sid}.txt').write_text(prompt)
    if '--cut-only' not in sys.argv:
        for attempt in range(1, 4):
            r = subprocess.run([sys.executable, str(ROOT / 'tools' / 'gen_image.py'), '--backend', 'azure', '--quality', 'medium' if white else 'high', *([] if white else ['--transparent']),
                                '--size', S['size'], '--prompt-file', str(STAGE / f'{sid}.txt'), str(sheet)], capture_output=True, text=True)
            if r.returncode: print(f'{sid}: generation failed — {r.stderr.strip()[-300:]}', flush=True); failed.append(sid); break
            problem = check(sheet, white, S['cols'], S['rows'], len(names))
            if not problem: break
            print(f'{sid}: try {attempt} rejected — {problem}', flush=True)
            sheet.rename(STAGE / f'{sid}-rejected{attempt}.png')
        else:
            print(f'{sid}: SKIPPED — three bad sheets, look at _staging/icons/{style}/{sid}-rejected*.png and fix the prompt', flush=True); failed.append(sid); continue
        if sid in failed: continue
    ASSETS.mkdir(parents=True, exist_ok=True)
    if white:
        cut = subprocess.run([sys.executable, str(ROOT / 'tools' / 'sheet_to_icons.py'), str(sheet), str(S['cols']), str(S['rows']), str(ASSETS), '--size', str(S['canvas']), *names], capture_output=True, text=True)
    else:
        cut = subprocess.run([sys.executable, str(ROOT / 'tools' / 'sheet_to_icons.py'), str(sheet), str(S['cols']), str(S['rows']), str(ASSETS), '--size', str(S['canvas']), '--alpha', *names], capture_output=True, text=True)
    bad = [l for l in cut.stdout.splitlines() if 'EMPTY' in l]
    print(f'{sid}: {len(names) - len(bad)}/{len(names)} cut' + (f' — {bad}' if bad else '') + (f'\n{cut.stderr[-300:]}' if cut.returncode else ''), flush=True)
    contact(sid, sheet, names, STAGE / f'{sid}-contact.png')
    print(f'   sheet → {sheet.relative_to(ROOT)}   contact → {(STAGE / f"{sid}-contact.png").relative_to(ROOT)}', flush=True)
if failed: print(f'\nsheets that need attention: {failed}', flush=True)
print(f'done: {len(want) - len(failed)} of {len(want)} sheets', flush=True)
