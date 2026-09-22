# Fantasy RPG Casual — style spec

Third skin of the same kit. Same class names, same `data-*`, same `sc.js`, same blocks and tests — only the CSS and
the icons differ. Built from the owner's reference images in `references/Fantasy RPG Casual/` (gitignored: look at,
never publish, never feed to a model). Ported from `tactical-dark/kit` (already token-driven), never written from memory.

## The one-line difference
Tactical Dark is a lit edge on a dark plate. Fantasy RPG Casual is a **chunky toy on a night-purple velvet**: thick
warm-dark outlines, matte rounded fills with a lighter top band, gold titles with an ornament line, pennants.

## What the references show
- **Ground**: deep purple-navy (`#241F3A`), tiles a step lighter (`#33304A`) with 14px rounded corners, no border.
- **Titles**: gold serif capitals, letter-spaced, with a thin gold line and a small diamond under them (Cinzel).
- **Icons**: thick warm dark-brown outline (`#2B1D1A`), one small top-left highlight, matte gradient, slight tilt.
- **Pennants**: hanging banners on a wooden rod with silver caps; V-shaped bottom; a darker band near the bottom.
- **Chests / packs**: painterly with sparkles and a colour glow — bigger shop art, not UI.
- Nothing else (buttons, toggles, sliders, popups) is in the references. Those follow the icon language: outline,
  matte fill, top band, rounded.

## Tokens (`core.css`) — same names as Tactical Dark, different values
| token | value | why |
|---|---|---|
| `--sc-font` | Baloo 2 800 (labels), Cinzel 700 (titles, in title.css) | round friendly labels, serif fantasy titles |
| `--sc-ground / well / panel / raise / edge` | `#241F3A / #1C1830 / #2E2949 / #3A3458 / #4E4874` | the velvet steps |
| `--sc-ink / dim` | `#FFF6E5 / #A79FC4` | warm white text, lilac secondary |
| `--sc-outline` | `#2B1D1A` | the icon outline, reused on every component edge |
| `--sc-line` | `2.5px` | thick, like the icons |
| `--sc-round` | `1.75` (→ 14px) | rounded tiles |
| `--sc-cut / --sc-spine` | `0 / 0` | no cut corners: that is Tactical Dark's shape |
| `--sc-glow` | `.35` | a little warmth, no neon |
| `--sc-button-fill` | `1.7` | solid accent buttons, not tinted glass |
| accents | sky `#3D8CF0` blue `#4C6CE8` green `#2DBF6A` yellow `#F2B21F` orange `#F07F2A` red `#D9333F` purple `#8A4CE8` pink `#E85BB5` … | pennant colours |

## Component notes (what differs from the Tactical Dark port)
- **Button**: dark outline (`--sc-outline`) instead of an accent border; fill = accent gradient with a lighter top band
  (`::after` top light stronger); label warm white with a soft dark shadow. No cut, no spine.
- **Title**: Cinzel, gold gradient text, ornament line + diamond underneath (`::after`), no glow ring.
- **Banner**: the pennant. Rod with silver caps on top (`::before`), V bottom via clip-path (reference-driven
  exception to the "no polygons" rule, like Tactical Dark's cuts), darker bottom band.
- **Slot / Shop card / Row**: tiles `--sc-raise` with 14px corners and NO border; the outline appears only on the item art.
- **Tag**: rounded pill with the dark outline.
- **Popup**: ornate plate — thick outline, gold inner hairline, four gold rivets in the corners (background
  layers, one element), Cinzel gold header with the ornament, thick bottom edge.
- **Toggle / Slider / Checkbox / Progress / Counter**: the chunky outlined family — dark outline, `--sc-well`
  trough with a bottom edge, accent fill with the button's top band, cream knobs with their own outline.
  Toggle and button share the light-fill rule: a dark label on gold/green/orange…, a light label on blue/red/purple.
- **Tabs**: an outlined trough; the selected tab is a gold chip with a dark label. **Tab bar**: outlined bar; the
  selected item sits on a raised outlined tile with a small gold cap.
- **Joystick**: outlined base, solid accent knob with outline and bottom edge.
- Everything else: tokens only.

## Rules from the owner (this style)
- **Text colour follows the icon colour.** The glyph icons are white, so every label is white — never a dark
  label, not even on a gold button. What makes white readable on gold is the same dark outline the icons have:
  labels on a fill get `-webkit-text-stroke` + `paint-order:stroke fill` in `--sc-outline`, and a white glyph on a
  fill gets a matching `drop-shadow` edge. (If a style ever uses black icons, its text goes black too.)
- **The outline is the element's own colour, darkest.** `--sc-outline` in core is a near-black cool neutral;
  every component redefines it for itself as `color-mix(<its colour> 38%, --sc-shade)` — a gold button has a
  dark-gold outline, a blue one dark-blue, a slate plate dark-slate. Never one brown line on everything.
- **The 3D underside is the element's own colour, darker, INSIDE the outline** (`inset 0 -N 0 …`), never a black
  slab under the shape. Applies to button, toggle, slider, checkbox, progress, counter, tabs, tab bar, joystick,
  popup. The top light is soft (three-stop gradient), not a hard band.

## Rules that carried over
1. Contrast first: labels near-white, accent carries state.
2. `:where()` defaults for `--line`.
3. No literal colours in component CSS — tokens or `color-mix()` steps (this style is themable from day one).
4. Port, don't rewrite. `python3 tools/check_style.py fantasy-rpg-casual` (+ `--layout`, `--order`, `--tests`).
5. Icons are generated images (Azure, `tools/icon_batch.py`), never code. 90 shared + the extension set.
