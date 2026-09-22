# Custom themes — the contract

**For Pixelfork AI (Astra).** Read this before giving a game a "Custom" look.

A player who likes neither ready-made style gets a **custom theme**: one small CSS file of design tokens,
loaded after a base style. The game's HTML does not change, the runtime does not change, the components do not
change. That is what makes the promise possible: **a themed game can be switched to Super Casual, Tactical Dark
or any other theme at any time by changing which CSS is loaded — nothing else.**

```html
<link rel="stylesheet" href="kit/kit.css">        <!-- the base style's bundle (tactical-dark/dist) -->
<link rel="stylesheet" href="theme.css">          <!-- the custom theme: tokens only -->
<script src="kit/kit.js"></script>
```

See it: `themes/preview.html` — the same ten screens under each theme, switched live.

## The two rules that keep a game switchable

1. **In the game: kit components + layout glue only.** Build every piece of UI from `sc-*` components
   (start from a block in `<style>/kit/blocks/`). Your own CSS may position things — `display`, `gap`, `width`,
   `position` — and nothing else. If glue needs a colour, a radius or a font it uses a token
   (`var(--sc-ground)`, `var(--sc-dim)`, `var(--sc-r)`, `var(--sc-font)`), never a literal.
2. **In the theme: tokens only.** One `:root { … }` block, plus at most one Google Fonts `@import`.
   No selectors, no component CSS, no `!important`, no images. If a look cannot be reached with tokens, it is
   not a theme — it is a new style (a different, bigger job: see `tactical-dark/STYLE.md`).

## Writing a theme

```css
/* theme: Neon Arcade · base: tactical-dark
   One line on the mood. */
@import url('https://fonts.googleapis.com/css2?family=Exo+2:wght@700;800&display=swap');
:root {
  --sc-font: 'Exo 2', 'Trebuchet MS', sans-serif;
  --sc-weight: 800;
  …
}
```

The first comment must name the base. Set only what differs from the base; everything else keeps its default.
The authoritative token list, with defaults, is the `THEME TOKENS` part of `<base>/kit/core.css`.

| Group | Tokens | What they do |
|---|---|---|
| Surfaces | `--sc-ground` `--sc-well` `--sc-panel` `--sc-raise` `--sc-edge` | page · inset areas (bar tracks, slot insides) · popups and bars · raised neutral tiles · neutral borders |
| Text | `--sc-ink` `--sc-dim` | main and secondary text |
| Accents | `--sc-c-sky` `blue` `cyan` `mint` `green` `olive` `yellow` `orange` `red` `pink` `purple` `white` `dark`, and `--sc-accent` | ONE value per colour name — fills, glows and tinted text are derived. Keep each name's meaning (green = go, red = danger, yellow = main action / gold) so games stay readable after a switch. `--sc-accent` is what a component uses with no `data-color`: point it at one of yours, `var(--sc-c-pink)` |
| Button | `--sc-button-tint` `--sc-button-label` `--sc-button-fill` | the fill is the accent mixed into the tint; `fill` 1 = tinted glass, up to 1.72 = solid accent |
| Shape | `--sc-round` `--sc-cut` `--sc-spine` `--sc-line` | roundness 0…8 (1 = base, 6 = pills) · button cut corner 0….45 · button's thick left edge 0….2 · line width |
| Light | `--sc-glow` | 0 = matte … 2.5 = neon |
| Type | `--sc-font` `--sc-weight` `--sc-caps` `--sc-tracking` | the weight must be one the `@import` loads; caps `uppercase` or `none`; tracking 0…2 |
| Light themes only | `--sc-sheen` `--sc-shade` `--sc-scrim` `--sc-glyph-filter` `--sc-glyph-on-button` | see below |

### A light theme needs five more tokens
The base is dark, so four things assume it. A light theme turns them around:
`--sc-sheen` (the highlight laid over surfaces: make it dark), `--sc-shade` (what surfaces darken with: a soft
grey-blue, or they go muddy), `--sc-scrim` (the veil behind popups and result screens — text sits on it, so make it
light), `--sc-glyph-filter: brightness(0) invert(.12)` (the white glyph icons become dark), and keep
`--sc-glyph-on-button: none` when button labels stay white. `themes/daylight/theme.css` is the worked example.

## Check it — always
```bash
python3 tools/check_theme.py themes/<name>/theme.css
```
It fails a theme that uses anything but tokens, sets a token the base does not have, leaves a number out of range,
names a font weight that is not loaded — and it **computes contrast the way the browser will**: text on all five
surfaces (7:1), secondary text (4.5:1), every accent against the surfaces it sits on (3:1), tinted text on its own
fill (4.5:1), and the label of a button in each colour against that button's fill (3:1, advice at 4.5:1).
A theme ships only on `PASS`. When it fails, change the token it names and run it again.

## What a theme cannot do (yet)
- **Icons stay the base style's.** New artwork is generated images, never code — a separate step.
- **Shapes stay the base style's**, within the knobs above. Glossy 3D, outlined text, a different button
  silhouette: that is a style, not a theme.
- **Only `tactical-dark` is themable today.** Super Casual has not been moved onto tokens.
- A font much wider than the base can crowd labels; the kit shrinks most labels to fit, so check the blocks.

## Examples
| Theme | Proves |
|---|---|
| `neon-arcade` | colour + pills + heavy glow, no cut corners |
| `desert-ops` | warm palette, square and matte, condensed type |
| `daylight` | a **light** theme on a dark base |
