# Cozy Paper — style spec

Sixth skin of the same kit. Same class names, same `data-*`, same `sc.js`, same blocks and tests. Ported from
`clean-flat/kit` (the light base, already one-colour-per-button and coloured tab bars), then warmed.

## The one-line difference
Warm cream paper with a real paper grain, soft painted icons, gentle earthy colour, a stitched seam on popups,
friendly hand-lettered type. Calm and homely.

## Fits
Farming, cozy life sims, cooking, café and restaurant, merge, story and choice, kids, pets, gardening.

## Tokens (`core.css`)
| token | value | why |
|---|---|---|
| `--sc-font` / `--sc-title-font` | Grandstander 700–800 / Chewy | friendly and hand-made; Grandstander's digits are all distinct (checked with Sniglet, Sour Gummy, Mali, Itim) |
| ground / well / panel / raise / edge | `#F6EEDF / #EADCC2 / #FFF8EC / #FFFBF4 / #D6C19C` | cream paper steps |
| ink / dim | `#3F2E22 / #7A6450` | warm dark text |
| `--sc-outline` | `#DDC9A6` | a light tan edge on neutral paper; coloured elements use their own colour, darker |
| accents | green `#5C973F` sky `#258DD3` red `#E0565B` orange `#D86819` gold `#B67C15` purple `#9A72C9` … | earthy, each tuned so a WHITE label reads ≥3:1 |
| `--sc-glyph-filter` | `brightness(0) invert(.2) sepia(.5)` | white glyphs become warm dark brown on paper |

## Paper
`assets/textures/paper.webp` — generated with Azure (a seamless cream watercolour paper), then made seamless by
blending with a half-offset copy (edge jump 7.3 vs 6.2 inside). 10 KB, tiled at 256px, `multiply`-blended under the
paper surfaces (popup, panel, slot, shop card, row, toast, solid screen). The rule lives in `core.css`, because a
`url()` resolves against the stylesheet that USES it (tested: a url in a custom property broke from components/).
Components set only `background-color` on those surfaces so they never reset the image.

## Carried over from Clean Flat (owner rules)
One colour per button (icon and text match; fix contrast by changing the fill) · tab bars use coloured icons ·
counter icon inside the pill · concentric "+" · ringed badge · solid icon buttons.

## Icons
Azure, `tools/icon_batch.py cozy-paper`: soft painted items with an outline in a darker shade of their own colour
(never black, never one brown line), pillowy glyphs, the 90 shared names, 36 farming / cooking / animal items,
the coloured navigation set N1, and shop art (coin and gem baskets, crates). Original designs only.
