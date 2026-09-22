# Image prompts: Fantasy RPG Casual style

Use these when a game needs a picture the kit doesn't have (a new item, character, currency, pack…).
Generate with `python3 tools/gen_image.py --backend azure --quality high`, then cut the background with
`python3 tools/cut_bg.py`. **Never draw pictures with code** (CSS/SVG/canvas). Always generate an image.

The 90 icons in this folder came from ten 3x3 sheets — see `ICON-SHEETS.md` — made with `tools/icon_batch.py`.
For a new icon that should match them, add it to a new sheet there (nine at a time keep the style consistent)
rather than generating it alone.

## 1. Style block — paste it into every prompt, word for word

Items (colour, on white):
```
Style: casual fantasy RPG inventory icon, like a polished mid-core mobile RPG shop. Clean cartoon rendering with a thick
dark outline (warm dark brown, almost black, about 3% of the icon size) around every shape. Soft, mostly matte shading:
smooth gradients, one small crisp highlight on the top-left, a slightly darker bottom edge — calm, not glossy, not candy.
Warm gold with an orange shadow, cool steel with a blue-grey shadow, gems with a few flat facets and one white glint.
Colours saturated and cheerful but a little muted. Slight three-quarter tilt, chunky and simplified. No text, no letters,
no numbers, no logos, no hands, no background scenery, no shadow on the ground, on one continuous field of solid pure white.
```

Glyphs (white, on black):
```
Style: classic game UI function glyph. ONE SOLID FILLED shape in pure flat white, bold and simple, with softly rounded
corners. Never line art, never outlined, never thin, no gradients, no shading, no 3D. No text. On one continuous field of
solid pure black.
```

## 2. One icon
```
A single game item icon of {subject}, {main colours}, centred with generous empty space around it (the object fills
about 80% of the image). {STYLE BLOCK}
```
Then: `python3 tools/cut_bg.py in.png out.png` (colour) or `--mono` (glyph), and `python3 tools/normalize_icons.py <folder>`.

## 3. Bigger shop art (packs, chests, bundles)
The reference packs are more painterly than the icons: add "soft painted rendering, small sparkles, a faint coloured
glow behind the object" to the item style block and keep the outline. Use 1536x1024 for a wide pack row.
