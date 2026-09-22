"""
Check a custom theme before it reaches a player.

  python3 tools/check_theme.py themes/neon-arcade/theme.css
  python3 tools/check_theme.py --base tactical-dark          # the base style's own defaults, as a sanity check

A theme is ONE :root block of tokens (plus an optional Google Fonts @import) loaded after a base style.
This verifies three things an AI-written theme gets wrong:
  1. SHAPE      only tokens the base declares, nothing else — no selectors, no components, no !important.
                That is what keeps a themed game switchable to any other style later.
  2. CONTRAST   computed the way the browser will compute it (same color-mix steps the CSS uses):
                text on every surface, secondary text, every accent against the surfaces it sits on,
                and the label of a button in each of the 13 colours against that button's fill.
  3. RANGE      numeric tokens inside the span the components were built for; the font weight actually loaded.
Exit code 1 on any FAIL. WARN is advice.
"""
import pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
COLOURS = ['sky', 'blue', 'cyan', 'mint', 'green', 'olive', 'yellow', 'orange', 'red', 'pink', 'purple', 'white', 'dark']
LOCKED = {'--sc-r', '--sc-button-label-mix', '--sc-button-dark-label', '--sc-label-outline', '--sc-safe-top', '--sc-safe-right', '--sc-safe-bottom', '--sc-safe-left', '--sc-tip-x', '--sc-tip-y',
          '--sc-min-text', '--sc-text-stroke', '--sc-text-drop', '--sc-outline'}       # derived, device or artwork facts — not taste
RANGES = {'--sc-round': (0, 8), '--sc-cut': (0, .45), '--sc-spine': (0, .2), '--sc-glow': (0, 2.5), '--sc-tracking': (0, 2),
          '--sc-button-fill': (.5, 1.72), '--sc-weight': (400, 900)}

def root_block(css):
    m = re.search(r':root\s*\{(.*?)\}', re.sub(r'/\*.*?\*/', '', css, flags=re.S), flags=re.S)
    return dict((k.strip(), v.strip()) for k, v in (d.split(':', 1) for d in m.group(1).split(';') if ':' in d)) if m else {}

def hex_rgb(v):
    v = v.strip().lstrip('#')
    if len(v) == 3: v = ''.join(c * 2 for c in v)
    return tuple(int(v[i:i + 2], 16) / 255 for i in (0, 2, 4))
def mix(a, b, p): return tuple(a[i] * p + b[i] * (1 - p) for i in range(3))
def lum(c):
    f = lambda x: x / 12.92 if x <= .03928 else ((x + .055) / 1.055) ** 2.4
    return .2126 * f(c[0]) + .7152 * f(c[1]) + .0722 * f(c[2])
def ratio(a, b):
    la, lb = sorted((lum(a), lum(b)), reverse=True); return (la + .05) / (lb + .05)

args = [a for a in sys.argv[1:] if not a.startswith('--')]
fails, warns = [], []
if '--base' in sys.argv:
    base, theme, name = args[0], {}, f'{args[0]} (defaults)'
else:
    path = pathlib.Path(args[0]); css = path.read_text(); name = str(path)
    m = re.search(r'base:\s*([a-z0-9-]+)', css)
    if not m: raise SystemExit('FAIL  the first comment must name the base style:  /* theme: My Theme · base: tactical-dark */')
    base = m.group(1)
    theme = root_block(css)
    # 1. shape
    bare = re.sub(r'/\*.*?\*/', '', css, flags=re.S)
    rest = re.sub(r':root\s*\{.*?\}', '', bare, flags=re.S)
    rest = re.sub(r"@import url\('https://fonts\.googleapis\.com/[^']+'\);", '', rest).strip()
    if rest: fails.append(f'only @import (Google Fonts) and one :root block are allowed — found: {rest[:70]!r}')
    if '!important' in bare: fails.append('!important is not allowed')
    if 'url(' in re.sub(r"@import url\([^)]*\);", '', bare): fails.append('no url() inside tokens (no images, no remote files)')

defaults = root_block((ROOT / base / 'kit' / 'core.css').read_text())
allowed = {k for k in defaults if k.startswith('--sc-')} - LOCKED
for k in theme:
    if k not in allowed: fails.append(f'{k} is not a theme token of {base}' + (' (it is derived or fixed)' if k in LOCKED else ''))
tok = {**defaults, **theme}

def colour(key, seen=()):
    v = tok[key] if key.startswith('--') else key
    m = re.fullmatch(r'var\((--[a-z0-9-]+)\)', v)
    if m: return colour(m.group(1))
    if not re.fullmatch(r'#[0-9a-fA-F]{3}|#[0-9a-fA-F]{6}', v): fails.append(f'{key}: {v!r} must be a #rrggbb colour or var(--sc-c-…)'); return (0, 0, 0)
    return hex_rgb(v)
def num(key):
    try: return float(tok[key])
    except ValueError: fails.append(f'{key}: {tok[key]!r} must be a number'); return 1

# 3. ranges + font
for k, (lo, hi) in RANGES.items():
    if not lo <= num(k) <= hi: fails.append(f'{k}: {tok[k]} is outside {lo}…{hi}')
if theme.get('--sc-font'):
    first = re.match(r"\s*'([^']+)'", theme['--sc-font'])
    imp = re.search(r"family=([^:&']+)(?::wght@([\d;]+))?", css)
    if first and (not imp or imp.group(1).replace('+', ' ') != first.group(1)): fails.append(f"--sc-font starts with '{first.group(1)}' but no matching Google Fonts @import loads it")
    elif imp and imp.group(2) and str(int(num('--sc-weight'))) not in imp.group(2).split(';'):
        fails.append(f"--sc-weight {tok['--sc-weight']} is not one of the loaded weights ({imp.group(2)}) — the browser would fake it")
    if 'sans-serif' not in theme['--sc-font'] and 'serif' not in theme['--sc-font'] and 'monospace' not in theme['--sc-font']: warns.append('--sc-font has no generic fallback (sans-serif)')
if theme.get('--sc-caps') not in (None, 'uppercase', 'none'): fails.append('--sc-caps must be uppercase or none')

# 2. contrast
ink, dim, ground = colour('--sc-ink'), colour('--sc-dim'), colour('--sc-ground')
surfaces = {s: colour('--sc-' + s) for s in ('ground', 'well', 'panel', 'raise', 'scrim')}
rows, soft_labels = [], []
def need(label, a, b, floor, hard=True):
    r = ratio(a, b); rows.append((label, r, floor))
    if r < floor: (fails if hard else warns).append(f'contrast {label}: {r:.2f} < {floor}')
for s, c in surfaces.items(): need(f'text on {s}', ink, c, 7)
for s in ('ground', 'panel'): need(f'secondary text on {s}', dim, surfaces[s], 4.5)
need('divider on panel', colour('--sc-edge'), surfaces['panel'], 1.25, hard=False)
fill = num('--sc-button-fill'); tint, blabel = colour('--sc-button-tint'), colour('--sc-button-label')
for n in COLOURS:
    c = colour('--sc-c-' + n)
    soft = n in ('dark',)                                  # the quiet neutral: allowed to recede
    need(f'{n} accent on panel', c, surfaces['panel'], 3, hard=not soft)
    need(f'{n} accent on ground', c, ground, 3, hard=not soft)
    need(f'{n} tinted text on its fill', mix(c, ink, .5), mix(c, ground, .12), 4.5)
    if n != 'dark':                                        # the dark button has its own neutral fill and label in the base
        # Button labels are large bold display text: WCAG's large-text floor (3:1) is the rule, 4.5:1 the advice.
        # Measured where the label sits — the middle of the top→bottom fill gradient.
        lmix = num('--sc-button-label-mix') / 100 if '--sc-button-label-mix' in tok else .35
        darks = tok.get('--sc-button-dark-label', '').strip("'\" ").split()
        label = colour('--sc-outline') if n in darks else mix(c, blabel, lmix)
        mid = mix(c, tint, min(1, .44 * fill))
        if tok.get('--sc-label-outline', 'none').strip() not in ('none', ''):
            # outlined labels (paint-order stroke): the letter meets its outline, and the outline meets the fill
            # readable if the letter itself clears the fill, OR its outline separates it from the fill
            o = colour('--sc-label-outline')
            ok = ratio(label, mid) >= 3 or (ratio(label, o) >= 4.5 and ratio(o, mid) >= 3)
            rows.append((f'{n} button label (outlined)', max(ratio(label, mid), min(ratio(label, o), ratio(o, mid))), 3))
            if not ok: fails.append(f'contrast {n} button label: {ratio(label, mid):.2f} on the fill and its outline only {ratio(o, mid):.2f} against the fill')
        else:
            need(f'{n} button label', label, mid, 3)
            if ratio(label, mid) < 4.5: soft_labels.append(f'{n} {ratio(label, mid):.1f}')

if soft_labels: warns.append('button labels under 4.5:1 (fine for large bold text, tight on data-size="sm"): ' + ', '.join(soft_labels))
worst = sorted(rows, key=lambda r: r[1] / r[2])[:6]
print(f'{name}  ·  base {base}  ·  {len(theme)} tokens set  ·  {len(rows)} contrast pairs')
for label, r, floor in worst: print(f'   tightest: {label:42} {r:5.2f}  (needs {floor})')
for w in warns: print('WARN ', w)
for f in fails: print('FAIL ', f)
print('PASS' if not fails else f'{len(fails)} problem(s)')
sys.exit(1 if fails else 0)
