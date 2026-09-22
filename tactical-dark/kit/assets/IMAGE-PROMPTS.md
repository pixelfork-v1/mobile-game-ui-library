# Icon prompts — Tactical Dark

88 flat white glyphs. **Generate them on a sheet, never one at a time** — icons made in separate calls drift
apart in weight and detail, which is exactly how the first attempt at this set went wrong. A 4x4 sheet gives
the model all 16 in one frame, so it keeps them a family.

    python3 tools/gen_image.py --prompt-file _staging/sheet.txt _staging/sheet-raw.png
    python3 tools/sheet_to_icons.py _staging/sheet-raw.png 4 4 tactical-dark/kit/assets name1 name2 ...
    python3 tools/icon_offsets.py tactical-dark/kit/assets tactical-dark/kit/assets/offsets.css
    python3 tools/sync_style.py tactical-dark "Tactical Dark"

`sheet_to_icons.py` turns brightness into alpha (so holes inside a glyph come out transparent), assigns each
white shape to its cell, and puts every icon on one 160x160 canvas scaled by how much ink it has — not by its
bounding box, or a wide arrow would read as heavy as a square chest.

## Style block — paste it into every sheet prompt, word for word

Kept in `_staging/_style.txt`. Two lines in it are load-bearing:

- **"The whole image is one single continuous field of solid pure black from edge to edge."** Without this the
  model draws each icon on its own black tile with white gutters between them, and the crop comes out as 16
  black squares. Do not phrase this as "no boxes" — naming boxes puts boxes in. Say what the background IS.
- **"ONE SOLID FILLED white shape ... never line art, never an outlined shape."** Anything with interior
  structure (a coin, a gem, a chest, a shop) reverts to outlines unless this is stated, and stated again for
  those specific icons.

Roughly one sheet in three still comes back tiled. Check before cutting:

    python3 -c "from PIL import Image; import numpy as np; a=np.asarray(Image.open('_staging/sheet-raw.png').convert('L')); w=a.shape[1]; print(a[:, int(w*.245):int(w*.255)].mean())"

Above ~40 means tiled — generate again, the prompt does not need changing.

## The set

| Sheet | Icons |
|---|---|
| A — interface | settings pause close play home shop arrow-left check search lock mail chat calendar avatar video gift |
| B — resources | coin gem heart energy star trophy chest key crown clover ticket cash ruby helmet ring arrow-right |
| C — survival gear | rifle pistol knife grenade ammo vest gas-mask medkit bandage fuel food water radio backpack map radar |
| D — status | warning skull shield clock plus minus refresh trash info wrench fire battery wifi compass crosshair crystal-ball |
| E — game | sound sound-off music-off menu restart star-empty heart-empty hand medal sword bomb rocket potion coin-pile |
| F — extras | music gem-pile alert level-badge fireball jump flag pin hourglass |

`back.png` is a copy of `arrow-left.png`.
