"""
Put every icon on the same square canvas at the same optical size.

Two icons look wrong side by side when each is merely cropped to its own outline: a wide arrow ends up as wide
as a square chest, and a thin key looks small next to a fat heart. This scales each glyph by how much ink it
actually has (area), not by its bounding box, then clamps so nothing overflows, and centres it on one canvas.
After this every icon file is the same pixel size and needs no per-icon offset.

  python3 tools/normalize_icons.py <folder> [--size 160] [--ink 0.34] [--box 0.86]
"""
import argparse, pathlib
import numpy as np
from PIL import Image

ap = argparse.ArgumentParser()
ap.add_argument('folder'); ap.add_argument('--size', type=int, default=160)
ap.add_argument('--ink', type=float, default=.34, help='target share of the canvas the glyph should cover')
ap.add_argument('--box', type=float, default=.86, help='the glyph may never be wider/taller than this share')
a = ap.parse_args()

S = a.size
for p in sorted(pathlib.Path(a.folder).glob('*.png')):
    im = Image.open(p).convert('RGBA')
    box = im.split()[-1].point(lambda v: 255 if v > 8 else 0).getbbox()
    if not box:
        print(f'{p.stem:14} empty, skipped'); continue
    im = im.crop(box)
    alpha = np.asarray(im.getchannel('A'), dtype=np.float32) / 255.0
    ink = float(alpha.sum())                                   # how much the glyph actually paints
    by_ink = (a.ink * S * S / max(ink, 1)) ** .5               # scale so ink ≈ the target share of the canvas
    by_box = a.box * S / max(im.width, im.height)              # … but never let it outgrow the canvas
    k = min(by_ink, by_box)
    w, h = max(1, round(im.width * k)), max(1, round(im.height * k))
    glyph = im.resize((w, h), Image.LANCZOS)
    canvas = Image.new('RGBA', (S, S), (0, 0, 0, 0))
    canvas.paste(glyph, ((S - w) // 2, (S - h) // 2), glyph)
    canvas.save(p, optimize=True)
    print(f'{p.stem:14} {w}x{h} on {S}x{S}   {"box-capped" if by_box < by_ink else "ink-matched"}')
