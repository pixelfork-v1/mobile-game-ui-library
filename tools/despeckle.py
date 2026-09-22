"""
Drop bits that are not part of the icon: stray lines, dots and crop-edge artefacts an image model leaves behind.
Keeps every shape at least --keep of the biggest one's area (so a two-part icon like "pause" survives), then re-crops.

  python3 tools/despeckle.py icon.png [--keep 0.06] [--pad 6]
"""
import argparse
from collections import deque
import numpy as np
from PIL import Image

ap = argparse.ArgumentParser()
ap.add_argument('path'); ap.add_argument('--keep', type=float, default=.06); ap.add_argument('--pad', type=int, default=6)
a = ap.parse_args()

im = Image.open(a.path).convert('RGBA')
arr = np.array(im); solid = arr[..., 3] > 40
h, w = solid.shape
lab = np.zeros((h, w), np.int32); sizes = [0]
for y in range(h):
    for x in range(w):
        if solid[y, x] and not lab[y, x]:
            cid = len(sizes); q = deque([(y, x)]); lab[y, x] = cid; n = 0
            while q:
                cy, cx = q.popleft(); n += 1
                for ny, nx in ((cy+1, cx), (cy-1, cx), (cy, cx+1), (cy, cx-1)):
                    if 0 <= ny < h and 0 <= nx < w and solid[ny, nx] and not lab[ny, nx]:
                        lab[ny, nx] = cid; q.append((ny, nx))
            sizes.append(n)
if len(sizes) < 3:
    raise SystemExit(f'{a.path}: one shape, nothing to clean')
big = max(sizes)
keep = {i for i, n in enumerate(sizes) if i and n >= big * a.keep}
dropped = len(sizes) - 1 - len(keep)
arr[..., 3] = np.where(np.isin(lab, list(keep)), arr[..., 3], 0)
img = Image.fromarray(arr, 'RGBA')
box = img.split()[-1].point(lambda v: 255 if v > 8 else 0).getbbox()
img = img.crop((max(0, box[0] - a.pad), max(0, box[1] - a.pad), min(w, box[2] + a.pad), min(h, box[3] + a.pad)))
img.save(a.path, optimize=True)
print(f'{a.path}: dropped {dropped} stray bit(s) → {img.size[0]}x{img.size[1]}')
