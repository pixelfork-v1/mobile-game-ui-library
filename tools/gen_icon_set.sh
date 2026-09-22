#!/bin/bash
# Generate one icon set for a style. Usage: bash tools/gen_icon_set.sh <out-dir> <size>
set -u
OUT=${1:-styles/tactical-dark/assets}; SIZE=${2:-160}
STYLE='Style: a SOLID FILLED pure white (#FFFFFF) silhouette on a solid pure black (#000000) background, like a stencil or a font glyph. It must be one solid white shape — NOT line art, NOT an outlined shape, NOT a white outline around a black interior. No black lines, marks or details drawn inside the white shape, except a hole where the description explicitly asks for one. Clean geometric construction, even weight, slightly technical, rounded ends on any stroke. No border, no frame, no shadow, no gradient, no glow, no 3D, no perspective, no text, no letters, no numbers. Centred, the glyph fills about 70% of the frame.'
TMP=$(mktemp -d)
gen () {
  name=$1; subject=$2
  echo "── $name"
  python3 tools/gen_image.py "A single user interface icon of $subject. $STYLE" "$TMP/$name.png" >/dev/null || { echo "   FAILED to generate"; return; }
  python3 tools/cut_bg.py "$TMP/$name.png" "$OUT/$name.png" --mono --pad 6 >/dev/null || { echo "   FAILED to cut"; return; }
  python3 - "$OUT/$name.png" "$SIZE" <<'PY'
import sys; from PIL import Image
p, s = sys.argv[1], int(sys.argv[2])
im = Image.open(p); im.thumbnail((s, s), Image.LANCZOS); im.save(p, optimize=True); print(f'   {im.size[0]}x{im.size[1]}')
PY
}
mkdir -p "$OUT"
gen settings "a gear wheel with six chunky square teeth, solid white, with one round hole cut out of its centre"
gen pause    "two vertical rounded bars side by side, a pause symbol"
gen close    "an X symbol made of exactly two straight bars of equal thickness crossing at right angles, solid white, rounded ends, nothing else in the frame"
gen play     "a solid triangle pointing right with slightly rounded corners, a play symbol"
gen shop     "a shop front seen from the front: a solid filled white rectangular building with a scalloped awning across the top, and one small arched doorway cut out of the lower middle"
gen home     "a house seen from the front: one solid filled white shape made of a square body with a triangular roof on top, and one small arched doorway cut out of the bottom middle"
gen back     "an arrow pointing left with a straight shaft"
gen check    "a tick mark, a check symbol, with rounded ends"
gen coin     "a coin seen face on: a solid filled white circle with a narrow ring groove near its edge and a small five-pointed star cut out of its centre"
gen gem      "a cut gem seen face on: a solid filled white shape with a flat top edge, angled shoulders and a pointed bottom, with two thin facet lines cut out of it"
gen heart    "a heart, one solid filled white shape, symmetrical, with a small notch at the top"
gen energy   "a lightning bolt, one solid filled white zigzag shape"
gen star     "a five-pointed star, one solid filled white shape with slightly rounded points"
echo "done → $OUT"
