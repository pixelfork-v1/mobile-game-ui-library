# Neon Cyber — style spec

Seventh skin of the same kit. Same class names, same `data-*`, same `sc.js`, same blocks and tests. Ported from
`clean-flat/kit` (it carries every owner rule), then turned dark: glass surfaces, glowing neon edges.

## The one-line difference
Deep navy-black, controls made of dark glass tinted by their neon colour, a neon edge and a soft glow, a faint grid on
solid screens. Loud colour, quiet surfaces.

## Fits
Space shooters, racing, rhythm and music, sci-fi puzzle, cyberpunk, arcade, esports-flavoured casual.

## Tokens (`core.css`)
| token | value | why |
|---|---|---|
| `--sc-font` / `--sc-title-font` | Oxanium 600–800 / Audiowide | technical and readable; Oxanium's digits all distinct (compared with Exo 2, Rajdhani, Saira, Orbitron) |
| ground / well / panel / raise / edge | `#070818 / #0B0E24 / #111536 / #181D47 / #333B78` | deep navy steps |
| ink / dim | `#EAF6FF / #8B97D1` | cool white, lavender secondary |
| accents | cyan `#00E5FF` magenta `#FF4FD8` green `#39FF88` yellow `#FFE14D` red `#FF3D6E` purple `#A77BFF` … | full neon — they are never a text background, so they can be bright |
| `--sc-button-fill` | `.5` | coloured controls are GLASS (the neon at ~26–34% over the well) |
| `--sc-glow` | `1.6` | strong, but kept close to the element |
| `--sc-glyph-filter` | `none` | dark style: white glyphs stay white |

## Rules (carried over and enforced)
- **One colour per button**: white text + white icon on every coloured control; the neon is the edge and the glow,
  the fill is dark glass, so contrast is always high. `data-color="dark"` is a slate plate with ink text.
- **Tabs use coloured icons**: N1 + N2 coloured nav sets, mapped by `--sc-nav-icons`.
- Counter icon inside the pill, concentric "+", ringed badge (from Clean Flat).
- Glass instead of solid on: button, icon button, toggle ON, selected tab, checked checkbox, banner.

## Icons
Azure, `tools/icon_batch.py neon-cyber`: glossy neon items (dark metal and glass, emissive edges, glow kept tight),
precise chamfered glyphs, the 90 shared names, 27 sci-fi items (laser, plasma sword, energy cell, ship, crystals,
drone, robot, racer helmet, vinyl, portal…), N1 + N2 coloured nav sets, packs and loot capsules. Original designs only.
