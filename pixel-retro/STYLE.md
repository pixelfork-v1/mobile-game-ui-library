# Pixel Retro — style spec

Fourth skin of the same kit. Same class names, same `data-*`, same `sc.js`, same blocks and tests — only the CSS and
the icons differ. Ported from `fantasy-rpg-casual/kit` (token-driven, per-component outlines), never written from memory.

## The one-line difference
Everything is drawn in art pixels: square shapes with a one-pixel notch cut from each corner, flat colour, shading in
hard steps (a light pixel row on top, a dark two-pixel row at the bottom), pixel fonts, pixel-art icons.

## Fits
Roguelikes, platformers, arcade, idle and incremental, retro RPG, puzzle with a nostalgic skin.

## Tokens (`core.css`)
| token | value | why |
|---|---|---|
| `--sc-font` / `--sc-title-font` | Jersey 10 / Press Start 2P | readable pixel labels — every digit distinct (Pixelify Sans was tried: its 2 and 5 read as 8); arcade capitals for titles |
| palette | Sweetie 16 (GrafxKid, CC0) — ground `#1A1C2C`, panel `#333C57`, edge `#566C86`, ink `#F4F4F4` | a real 16-colour pixel palette, so everything sits together |
| `--sc-px` | `3px` | one art pixel: outlines, highlight rows, the corner notch |
| `--sc-notch` | an 8-step polygon | the classic 8-bit rounded rectangle, `clip-path` on child-free surfaces |
| `--sc-round` / `--sc-glow` / `--sc-cut` / `--sc-spine` | `0 / 0 / 0 / 0` | no curves, no glow, no bevels |
| `--sc-outline` | `#0B0C14` | near-black neutral outline; coloured elements use the dark of their own colour |

## Shape rules
- **Notch, not radius.** `border-radius:0` everywhere; `clip-path:var(--sc-notch)` on surfaces with no children that
  stick out (button, popup box, toggle, tag, checkbox box, slider track and knob, progress track, counter pill, row,
  toast). Surfaces that carry an attached tag or badge (slot, shop card, icon button) stay plain squares, or the
  notch would cut the badge off.
- **Hard shading only.** No gradients that blend: one light pixel row on top (`inset 0 var(--sc-px)`), a dark step at
  the bottom in the element's own colour, darker.
- **Segmented bars.** The progress fill is drawn in blocks (a mask), like an old HP bar.
- **Text follows the icons.** White labels with a hard four-way pixel outline and a one-pixel drop, in the dark of
  the element's colour. Titles: Press Start 2P with a hard drop shadow and a dashed pixel rule with a square under it.
- Joystick base and knob stay round: a round control reads better under the thumb.

## Icons
Generated with Azure (`tools/icon_batch.py pixel-retro`), never drawn in code. `ICON-SHEETS.md` = the 90 shared
names (same as every style, so games switch cleanly); `ICON-SHEETS-EXT.md` = retro extras (mushrooms, blocks,
pipes, ghosts, slimes, gems in five colours) and shop art (chests, coin and gem packs).

## Originality
Retro is full of famous shapes. Prompts ask for **generic** retro items and every sheet carries "Original designs
only — nothing that copies a character or item from an existing game". A first draft of the extension list had a
question block, a green pipe, a star with eyes, spotted 1-up mushrooms and an invader-style alien; they were replaced
(stone brick, barrel, crate, gold star, toadstool, one-eyed alien) before the sheets were generated or regenerated.
