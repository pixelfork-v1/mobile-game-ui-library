# Clean Flat — style spec

Fifth skin of the same kit and the first **light** one. Same class names, same `data-*`, same `sc.js`, same blocks and
tests. Ported from `fantasy-rpg-casual/kit` (token-driven, per-component edges and lips), then flattened.

## The one-line difference
White cards on a pale grey-blue ground, saturated flat colour, rounded shapes, soft shadows, no outlines, no gloss.
Colour carries meaning; everything else is quiet.

## Fits
Puzzle, word, trivia, merge, match-3 menus, idle, board and card, kids, sports, hyper-casual, cozy and wellness —
the widest range of any style, and the best base for Custom themes.

## Tokens (`core.css`)
| token | value | why |
|---|---|---|
| `--sc-font` / `--sc-title-font` | Nunito 800 / Fredoka 700 | round and friendly, clear digits |
| ground / well / panel / raise / edge | `#F2F5FA / #E4E9F2 / #FFFFFF / #F7F9FC / #C9D1DE` | pale steps; the panel is pure white |
| ink / dim | `#1C2333 / #5A6478` | dark text on light surfaces |
| `--sc-outline` | `#D9DFEA` | a light grey edge on neutral surfaces; coloured elements use their own colour, 80% |
| accents | sky `#108CFF` green `#2A9F47` yellow `#B38300` orange `#EF5F00` red `#FF4859` purple `#8C5CFF` … | each darkened from a bright base until a WHITE label reads 3:1 on it |
| `--sc-glyph-filter` | `brightness(0) invert(.16)` | white glyph icons turn dark slate on light surfaces; on coloured fills they stay white |
| `--sc-scrim` | `#EEF2F8` | a light veil behind popups and result screens (text sits on it) |
| `--sc-label-outline` | `none` | labels are not outlined — every white label must clear its fill on its own |
| `--sc-round` / `--sc-glow` | `2 / 0` | 16px corners, no glow |

## Shape rules
- **Popup** is a white card with a large soft shadow; header in Fredoka, ink colour.
- **Button** is solid colour with a softer lip (the colour at 76%) and a hairline edge in the same hue.
  `data-color="dark"` is the quiet secondary: white with a grey edge and a dark label.
- **Title** in the accent colour, no shadow, a short rounded bar under it. **Banner** is a plain rounded ribbon.
- **Text follows the icon colour**: dark labels and dark glyphs on light surfaces, white labels and white glyphs on
  coloured fills. The progress label is dark with a white halo because it straddles fill and track.

## Rules from the owner (this style)
- **Tab bars use coloured icons**, never white glyphs: `home-color`, `shop-color`, `settings-color`, `map-color`,
  `mail-color`, `calendar-color`, `profile-color`, `friends-color`, `quest-color` (sheet N1), plus any colour item.
- **Counter icons sit inside the pill**, and the "+" is a solid circle concentric with the pill's round end.
- **Badges**: a solid colour pill, white number, a white ring separating it from what it sits on, a soft shadow.
- **Solid icon buttons**: the default icon button is solid colour with a white glyph (a white glyph on a pale tint
  was unreadable). `flat` / `ring` variants stay light and their glyphs turn dark.

## Icons
Azure, `tools/icon_batch.py clean-flat`. Flat vector items (two or three tones, no outline) and rounded solid glyphs.
The 90 shared names + puzzle/word extras (hint, shuffle, hammer, magnet, bomb, sweets, fruit) + packs and gift boxes.
Original designs only.
