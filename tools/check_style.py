"""
Check that a style's CSS covers everything the reference style (super-casual) supports.

A style is a re-skin: every selector that carries BEHAVIOUR in the reference — a size, a position, a state,
a nested part sc.js builds — must have a counterpart, or that option silently does nothing. Writing a style's
CSS from memory dropped 60 of them; this finds them in a second.

  python3 tools/check_style.py tactical-dark            # selector coverage
  python3 tools/check_style.py tactical-dark --tests    # also build the kit's regression pages against the style
                                                        # → open http://localhost:8767/_staging/tests-<style>/index.html
  Failures there that assert Super Casual's own pixel sizes or colours are expected; behaviour must pass.
  python3 tools/check_style.py tactical-dark --order    # bundle vs. component files loaded in REVERSE order
                                                        # → open http://localhost:8767/_staging/order-compare.html?style=<style>
  Must say "0 differ". A difference is two rules in different files that tie on specificity, so the winner
  depends on load order — the bundle and a hand-linked page would then look different. Fix: make the host's
  rule stronger (.sc-shopcard > .sc-button.sc-shopcard-buy), never rely on order. Run build_kit.py first.
"""
import json, pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
style = sys.argv[1]
SRC = ROOT / 'super-casual' / 'kit' / 'components'
DST = ROOT / style / 'kit' / 'components'
core = (ROOT / style / 'kit' / 'core.css').read_text()
_rv = ROOT / style / 'style-check.json'          # gaps a human has looked at and accepted, with the reason
REVIEWED = set(json.loads(_rv.read_text())['reviewed']) if _rv.exists() else set()

def rules(css):
    css = re.sub(r'/\*.*?\*/', '', css, flags=re.S)
    css = re.sub(r'@keyframes[^{]+\{(?:[^{}]*\{[^{}]*\})*[^{}]*\}', '', css)
    out = []
    for m in re.finditer(r'([^{}]+)\{[^{}]*\}', css):
        for s in m.group(1).split(','):
            s = s.strip()
            if s and not s.startswith('@') and not re.match(r'^(from|to|\d+%)', s):
                out.append(s)
    return out

def parts(sel):
    t = set(re.findall(r'\.sc-[a-z-]+', sel))
    t |= set(re.findall(r'(?<![\w.-])(img|svg|path|button|fieldset)(?![\w-])', sel))
    t |= {a for a in re.findall(r'\[(data-[a-z-]+(?:[~|^$*]?="[^"]*")?|aria-[a-z]+(?:="[^"]*")?|disabled|hidden)', sel)
          if not a.startswith('data-color')}
    t |= {':' + x for x in re.findall(r':(disabled|active|focus-visible|first-child|last-child|nth-child)', sel)}
    return frozenset(t)

missing = 0
# an unclosed /* silently swallows declarations up to the next */ — cheap to catch, invisible in the browser
for f in [ROOT / style / 'kit' / 'core.css', *sorted(DST.glob('*/*.css'))]:
    s = f.read_text()
    if s.count('/*') != s.count('*/'):
        print(f'{f.relative_to(ROOT)}: UNBALANCED COMMENT ({s.count("/*")} opened, {s.count("*/")} closed)'); missing += 1
for d in sorted(SRC.iterdir()):
    a, b = d / f'{d.name}.css', DST / d.name / f'{d.name}.css'
    if not a.exists():
        continue
    if not b.exists():
        print(f'{d.name}: NOT SKINNED'); missing += 1; continue
    have = [parts(s) for s in rules(b.read_text() + core)]
    gaps = sorted({s for s in rules(a.read_text()) if parts(s) and s not in REVIEWED and not any(parts(s) <= h for h in have)})
    if gaps:
        missing += len(gaps)
        print(f'\n{d.name}:')
        for g in gaps: print('   ', g[:120])
print(f'\n{missing} uncovered selector(s)' if missing else f'every behavioural selector is covered ({len(REVIEWED)} reviewed exceptions in {style}/style-check.json)')

# --layout: same selector on both sides, but the style dropped a property that lays things out (not a colour).
# Selector coverage cannot see this: .sc-panel existed, it just no longer stretched. Read the list, don't chase zero.
LAYOUT = {'display', 'position', 'align-self', 'justify-self', 'flex', 'flex-direction', 'flex-wrap', 'box-sizing', 'width', 'min-width',
          'height', 'inset', 'left', 'right', 'top', 'bottom', 'z-index', 'pointer-events', 'overflow', 'grid-template-columns', 'white-space'}
def decls(css):
    css = re.sub(r'/\*.*?\*/', '', css, flags=re.S)
    out = {}
    for m in re.finditer(r'([^{}]+)\{([^{}]*)\}', css):
        props = {d.split(':')[0].strip() for d in m.group(2).split(';') if ':' in d}
        for s in m.group(1).split(','):
            out.setdefault(s.strip(), set()).update(props)
    return out
if '--layout' in sys.argv:
    for d in sorted(SRC.iterdir()):
        a, b = d / f'{d.name}.css', DST / d.name / f'{d.name}.css'
        if not (a.exists() and b.exists()): continue
        ref, got = decls(a.read_text()), decls(b.read_text())
        for sel, props in ref.items():
            lost = sorted((props & LAYOUT) - got.get(sel, props))
            if lost: print(f'{d.name}: {sel[:70]}  lost {", ".join(lost)}')

if '--tests' in sys.argv:
    out = ROOT / '_staging' / f'tests-{style}'
    out.mkdir(parents=True, exist_ok=True)
    for f in (ROOT / 'tools' / 'tests').glob('*.html'):
        (out / f.name).write_text(f.read_text().replace('../../super-casual/kit/', f'../../{style}/kit/'))
    print(f'regression pages built → http://localhost:8767/_staging/tests-{style}/index.html')

if '--order' in sys.argv:
    out = ROOT / '_staging'; out.mkdir(exist_ok=True)
    page = next((ROOT / s / 'kit' / 'examples' / 'all-components.html' for s in (style, 'tactical-dark')
                 if (ROOT / s / 'kit' / 'examples' / 'all-components.html').exists()))      # same markup serves every style
    src = page.read_text().replace('../assets/', f'../{style}/kit/assets/')
    links = re.findall(r'<link rel="stylesheet" href="\.\./components/[^>]+>\n?', src)
    bare = src
    for l in links: bare = bare.replace(l, '')
    rev = bare.replace('<link rel="stylesheet" href="../core.css">', '<link rel="stylesheet" href="../core.css">\n' + ''.join(reversed(links)))
    rev = rev.replace('"../core.css"', f'"../{style}/kit/core.css"').replace('../components/', f'../{style}/kit/components/').replace('"../sc.js"', f'"../{style}/kit/sc.js"')
    (out / f'order-rev-{style}.html').write_text(rev)
    (out / f'order-bundle-{style}.html').write_text(bare.replace('"../core.css"', f'"../{style}/dist/kit.css"').replace('"../sc.js"', f'"../{style}/dist/kit.js"'))
    (out / 'order-compare.html').write_text("""<!doctype html><meta charset="utf-8"><title>order compare</title>
<style>body{font:14px system-ui;background:#111;color:#ddd} iframe{width:420px;height:800px;border:0}</style><pre id="out">running…</pre>
<script>
const style = new URLSearchParams(location.search).get('style') || 'tactical-dark';
const load = src => new Promise(r => { const f = document.createElement('iframe'); f.src = src; f.onload = () => { const s = f.contentDocument.createElement('style'); s.textContent = '*,*::before,*::after{animation:none!important;transition:none!important}'; f.contentDocument.head.append(s); setTimeout(() => r(f), 2500); };   /* frozen: a pulsing icon is not an order bug */ document.body.append(f); });
const snap = f => [...f.contentDocument.querySelectorAll('[class*="sc-"]')].map(e => { const r = e.getBoundingClientRect(), c = getComputedStyle(e);
  return { k: e.className.toString().split(' ')[0] + (e.dataset.size ? '[' + e.dataset.size + ']' : ''), v: [Math.round(r.width), Math.round(r.height), c.fontSize, c.backgroundColor, c.borderTopWidth, c.color].join(' ') }; });
(async () => {
  const a = snap(await load('order-bundle-' + style + '.html')), b = snap(await load('order-rev-' + style + '.html'));
  const diff = []; if (a.length !== b.length) diff.push('element count ' + a.length + ' vs ' + b.length);
  a.forEach((x, i) => { if (b[i] && x.v !== b[i].v) diff.push(x.k + '   bundle: ' + x.v + '   reversed: ' + b[i].v); });
  out.textContent = style + ': ' + a.length + ' elements, ' + diff.length + ' differ\\n' + [...new Set(diff)].join('\\n');
  document.title = (diff.length ? 'FAIL' : 'PASS') + ' — order compare';
})();
</script>""")
    print(f'order pages built → http://localhost:8767/_staging/order-compare.html?style={style}')
