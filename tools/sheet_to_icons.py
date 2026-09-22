"""
Cut a generated icon SHEET (white glyphs on a flat black field) into separate transparent PNGs.

One step, so nothing drifts: brightness becomes alpha in place (no cropping, so the grid stays true), each
white shape is assigned to the cell its centre falls in, then every icon is centred on one square canvas at a
matched optical size — the same normalisation tools/normalize_icons.py does.

  python3 tools/sheet_to_icons.py SHEET COLS ROWS OUT_DIR name1 name2 … [--size 160] [--ink 0.34]
"""
import argparse
from collections import deque

import numpy as np
from PIL import Image

ap = argparse.ArgumentParser()
ap.add_argument('sheet'); ap.add_argument('cols', type=int); ap.add_argument('rows', type=int)
ap.add_argument('out'); ap.add_argument('names', nargs='+')
ap.add_argument('--size', type=int, default=160)
ap.add_argument('--ink', type=float, default=.34)
ap.add_argument('--box', type=float, default=.86)
ap.add_argument('--min-part', type=int, default=90, help='ignore blobs smaller than this many pixels')
ap.add_argument('--alpha', action='store_true',
                help="the sheet already has a transparent background: use its own alpha and keep each icon's "
                     'colours, instead of deriving alpha from brightness')
a = ap.parse_args()

src = Image.open(a.sheet).convert('RGBA')
rgb = np.asarray(src).astype(np.float32)[..., :3]
if a.alpha:
    alpha = np.asarray(src).astype(np.float32)[..., 3] / 255.0
else:
    lum = rgb.mean(axis=2) / 255.0
    lo, hi = .10, .92
    alpha = np.clip((lum - lo) / (hi - lo), 0, 1)             # white glyph on black → alpha
H, W = alpha.shape

solid = alpha > .45
S = 2
mask = solid[::S, ::S]
h, w = mask.shape
lab = np.zeros((h, w), np.int32); comps = []
for y in range(h):
    for x in range(w):
        if mask[y, x] and not lab[y, x]:
            cid = len(comps) + 1; q = deque([(y, x)]); lab[y, x] = cid; n = sy = sx = 0; y0 = y1 = y; x0 = x1 = x
            while q:
                cy, cx = q.popleft(); n += 1; sy += cy; sx += cx; y0 = min(y0, cy); y1 = max(y1, cy); x0 = min(x0, cx); x1 = max(x1, cx)
                for ny, nx in ((cy+1, cx), (cy-1, cx), (cy, cx+1), (cy, cx-1)):
                    if 0 <= ny < h and 0 <= nx < w and mask[ny, nx] and not lab[ny, nx]:
                        lab[ny, nx] = cid; q.append((ny, nx))
            comps.append((cid, n * S * S, sy / n * S, sx / n * S, (y0 * S, y1 * S, x0 * S, x1 * S)))

cw, ch = W / a.cols, H / a.rows
full = np.kron(lab, np.ones((S, S), np.int32))[:H, :W]
for i, name in enumerate(a.names):
    r, c = divmod(i, a.cols)
    mine = [(cid, n, cy, cx, bb) for cid, n, cy, cx, bb in comps if n > a.min_part and int(cy // ch) == r and int(cx // cw) == c]
    if mine:   # a stray speck from a neighbour (an ember, a spark) is small AND away from the drawing: drop it
        big = max(mine, key=lambda m: m[1]); rad = int(.06 * min(ch, cw) / S)
        def touches(m):            # is any pixel of the main drawing within `rad` of this part's own pixels?
            y0, y1, x0, x1 = (v // S for v in m[4])
            win = lab[max(0, y0 - rad):y1 + rad + 1, max(0, x0 - rad):x1 + rad + 1]
            return (win == big[0]).any()
        def at_edge(m):            # an intruder from a neighbouring cell sits in this cell's outer margin
            fy, fx = (m[2] - r * ch) / ch, (m[3] - c * cw) / cw
            return min(fy, 1 - fy, fx, 1 - fx) < .16
        mine = [m for m in mine if m[1] >= .12 * big[1] or touches(m) or not at_edge(m)]   # dots inside a glyph (crosshair, i, !) stay
    ids = [m[0] for m in mine]
    if not ids:
        print(f'{name:12} EMPTY CELL — check the sheet'); continue
    keep = np.isin(full, ids)
    cell = np.where(keep, alpha, 0)
    ys, xs = np.nonzero(cell > .03)
    y0, y1, x0, x1 = ys.min(), ys.max() + 1, xs.min(), xs.max() + 1
    glyph_a = cell[y0:y1, x0:x1]
    gh, gw = glyph_a.shape
    colour = (rgb[y0:y1, x0:x1].astype('uint8') if a.alpha            # keep the artwork's own colours
              else np.full((gh, gw, 3), 255, 'uint8'))                # flat glyph: paint it white
    img = Image.fromarray(np.dstack([colour, (glyph_a * 255).astype('uint8')]), 'RGBA')

    ink = float(glyph_a.sum())
    k = min((a.ink * a.size * a.size / max(ink, 1)) ** .5, a.box * a.size / max(gw, gh))
    nw, nh = max(1, round(gw * k)), max(1, round(gh * k))
    canvas = Image.new('RGBA', (a.size, a.size), (0, 0, 0, 0))
    g = img.resize((nw, nh), Image.LANCZOS)
    canvas.paste(g, ((a.size - nw) // 2, (a.size - nh) // 2), g)
    canvas.save(f'{a.out}/{name}.png', optimize=True)
    print(f'{name:12} parts={len(ids)}  {nw}x{nh} on {a.size}')
