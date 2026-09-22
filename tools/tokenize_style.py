"""
Turn a style's hardcoded colours into theme tokens, so a THEME (a handful of :root values) can recolour it.

  python3 tools/tokenize_style.py tactical-dark            # dry run: print the mapping table
  python3 tools/tokenize_style.py tactical-dark --write    # rewrite components/*/*.css

Every literal becomes the nearest token, corrected with color-mix so today's look is kept:
  #18223A  →  var(--sc-raise)                                   (exact)
  #101828  →  color-mix(in srgb, var(--sc-raise) 70%, #000)     (a darker step of the same surface)
  #3BA7FF  →  color-mix(in srgb, var(--sc-c-sky) 87%, #fff)     (a brighter step of the accent)
  #1e9cf559 → color-mix(in srgb, var(--sc-c-sky) 35%, transparent)
Black (shadows, backdrops) is left alone. Literals that fit nothing within tolerance are listed, not touched.
One-off tool: run once per style, review the diff, then maintain the tokens by hand.
"""
import colorsys, pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
style = sys.argv[1]
KIT = ROOT / style / 'kit'
core = (KIT / 'core.css').read_text()

def rgb(h):
    h = h.lstrip('#')
    if len(h) in (3, 4): h = ''.join(c * 2 for c in h)
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4)), (int(h[6:8], 16) / 255 if len(h) == 8 else 1)

TOKENS = {m.group(1): rgb(m.group(2))[0] for m in re.finditer(r'(--sc-(?:c-[a-z]+|ground|well|panel|raise|edge|dim|ink)):\s*(#[0-9a-fA-F]{6})', core)}
NEUTRAL = ['--sc-ground', '--sc-well', '--sc-panel', '--sc-raise', '--sc-edge', '--sc-dim', '--sc-ink']
FORCE = {'a3b4ff': 'color-mix(in srgb, var(--sc-c-blue) 56%, #fff)'}      # a pale accent the hue test mistakes for a grey
SKIP = {'420917', 'ffeab0'}                         # the button's own tint pair: tokens of their own, set by hand

def mix(a, b, p): return tuple(a[i] * p + b[i] * (1 - p) for i in range(3))
def dist(a, b): return sum((a[i] - b[i]) ** 2 for i in range(3)) ** .5

def is_neutral(c):
    h, s, v = colorsys.rgb_to_hsv(*(x / 255 for x in c))
    return v < .38 or s < .2 or (.56 < h < .64 and s < .45)

def fit(c):
    names = [n for n in TOKENS if (n in NEUTRAL) == is_neutral(c)]
    best = None
    for n in names:
        for other, oname in (((0, 0, 0), '#000'), ((255, 255, 255), '#fff')):
            for p in range(100, 39, -1):
                d = dist(mix(TOKENS[n], other, p / 100), c)
                if best is None or d < best[0] - .01: best = (d, n, p, oname)
    return best

def expr(hexlit):
    c, a = rgb(hexlit)
    if hexlit.lower().lstrip('#')[:6] in SKIP: return None, 0
    if c == (0, 0, 0): return None, 0                             # shadows and backdrops stay black
    if hexlit.lower().lstrip('#')[:6] in FORCE: e, d = FORCE[hexlit.lower().lstrip('#')[:6]], 0
    elif c == (255, 255, 255): e, d = 'var(--sc-sheen)', 0           # white = the highlight colour (a light theme makes it dark)
    else:
        d, n, p, o = fit(c)
        e = f'var({n})' if p == 100 else f'color-mix(in srgb, var({n}) {p}%, {o})'
    if a < 1: e = f'color-mix(in srgb, {e} {round(a * 100)}%, transparent)'
    return e, d

table, bad = {}, {}
files = sorted((KIT / 'components').glob('*/*.css'))
for f in files:
    for lit in set(re.findall(r'#[0-9a-fA-F]{3,8}\b', re.sub(r'/\*.*?\*/', '', f.read_text(), flags=re.S))):
        if len(lit) not in (4, 5, 7, 9) or lit.lower() in ('#0000',): continue
        e, d = expr(lit)
        if e is None: continue
        (table if d <= 25 else bad)[lit.lower()] = (e, d)      # 25 ≈ a shade you can only see side by side

for lit, (e, d) in sorted(table.items(), key=lambda x: x[1][0]): print(f'{lit:10} {d:5.1f}  {e}')
print(f'\n{len(table)} literals map within tolerance; {len(bad)} do not:')
for lit, (e, d) in sorted(bad.items()): print(f'  {lit:10} {d:5.1f}  nearest: {e}')

if '--write' in sys.argv:
    for f in files:
        parts = re.split(r'(/\*.*?\*/)', f.read_text(), flags=re.S)          # never touch comments
        for i in range(0, len(parts), 2):
            parts[i] = re.sub(r'#[0-9a-fA-F]{3,8}\b', lambda m: table.get(m.group(0).lower(), (m.group(0),))[0], parts[i])
        f.write_text(''.join(parts))
    print('written')
