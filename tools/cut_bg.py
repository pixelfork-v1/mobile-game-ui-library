"""
Turn a flat-background icon (e.g. from Gemini, which returns opaque PNGs) into a clean transparent PNG.

Why not a plain colour key: the highlight inside an icon is often the same white as the background, and a
global key eats it. This floods in from the edges instead, so only the outside is removed, and it un-blends
the soft edge pixels so no white halo is left around the dark outline.

Usage:
  python3 tools/cut_bg.py in.png out.png [--tol 30] [--pad 8]
"""
import argparse
from collections import deque

import numpy as np
from PIL import Image, ImageFilter

ap = argparse.ArgumentParser()
ap.add_argument('src'); ap.add_argument('out')
ap.add_argument('--tol', type=int, default=30, help='how far a pixel may differ from the corner colour and still count as background')
ap.add_argument('--pad', type=int, default=8, help='transparent margin left around the icon')
ap.add_argument('--mono', action='store_true',
                help='single-colour glyph on a flat background: alpha comes from brightness, so holes inside the '
                     'shape (a gear centre, a door) become transparent too, and the edge stays perfectly smooth')
ap.add_argument('--tint', default='#FFFFFF', help='--mono only: the colour the glyph is painted in')
a = ap.parse_args()

im = Image.open(a.src).convert('RGB')
arr = np.asarray(im).astype(np.int16)
h, w, _ = arr.shape
bg = np.median(np.concatenate([arr[0], arr[-1], arr[:, 0], arr[:, -1]]), axis=0)   # the frame's own colour

if a.mono:
    lum = arr.mean(axis=2) / 255.0
    dark_bg = float(np.mean(bg)) < 128
    alpha = np.clip(lum if dark_bg else 1.0 - lum, 0, 1)
    lo, hi = 0.10, 0.92                                   # ignore sensor-ish noise, treat near-white as solid
    alpha = np.clip((alpha - lo) / (hi - lo), 0, 1)
    tint = tuple(int(a.tint.lstrip('#')[i:i + 2], 16) for i in (0, 2, 4))
    rgb = np.zeros((h, w, 3), 'uint8'); rgb[..., 0], rgb[..., 1], rgb[..., 2] = tint
    img = Image.fromarray(np.dstack([rgb, (alpha * 255).astype('uint8')]), 'RGBA')
    box = img.split()[-1].point(lambda v: 255 if v > 8 else 0).getbbox()
    img = img.crop((max(0, box[0] - a.pad), max(0, box[1] - a.pad), min(w, box[2] + a.pad), min(h, box[3] + a.pad)))
    img.save(a.out, optimize=True)
    print(f'{a.out}  {img.size[0]}x{img.size[1]}  mono glyph, holes kept')
    raise SystemExit

close = (np.abs(arr - bg).max(axis=2) <= a.tol)
out = np.zeros((h, w), bool)                       # background reachable from the edge
q = deque()
for x in range(w):
    for y in (0, h - 1):
        if close[y, x] and not out[y, x]: out[y, x] = True; q.append((y, x))
for y in range(h):
    for x in (0, w - 1):
        if close[y, x] and not out[y, x]: out[y, x] = True; q.append((y, x))
while q:
    cy, cx = q.popleft()
    for ny, nx in ((cy+1, cx), (cy-1, cx), (cy, cx+1), (cy, cx-1)):
        if 0 <= ny < h and 0 <= nx < w and close[ny, nx] and not out[ny, nx]:
            out[ny, nx] = True; q.append((ny, nx))

alpha = np.where(out, 0.0, 1.0)
# the 2px ring just inside the object is background blended with the edge colour: recover how much is object
ring = np.asarray(Image.fromarray((out * 255).astype('uint8')).filter(ImageFilter.MaxFilter(5))) > 0
ring &= ~out
lum = arr.mean(axis=2)
bg_lum = float(np.mean(bg))
est = np.clip((bg_lum - lum) / max(bg_lum, 1.0), 0.0, 1.0) if bg_lum > 128 else np.clip((lum - bg_lum) / max(255 - bg_lum, 1.0), 0.0, 1.0)
alpha[ring] = np.maximum(est[ring], .12)

rgb = arr.astype(np.float32)
m = ring & (alpha > .02)                                     # un-blend: remove the background colour mixed in
for c in range(3):
    ch = rgb[..., c]
    ch[m] = np.clip((ch[m] - (1 - alpha[m]) * bg[c]) / alpha[m], 0, 255)
    rgb[..., c] = ch

res = np.dstack([rgb.astype('uint8'), (alpha * 255).astype('uint8')])
img = Image.fromarray(res, 'RGBA')
box = img.split()[-1].point(lambda v: 255 if v > 8 else 0).getbbox()
img = img.crop((max(0, box[0] - a.pad), max(0, box[1] - a.pad), min(w, box[2] + a.pad), min(h, box[3] + a.pad)))
img.save(a.out, optimize=True)
print(f'{a.out}  {img.size[0]}x{img.size[1]}  background removed (corner colour {tuple(int(v) for v in bg)})')
