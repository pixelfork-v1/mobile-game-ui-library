# Icon sheet prompts — Pixel Retro

Ten sheets, nine icons each, 3x3, square image. Same names as the other styles (so games stay switchable),
retro RPG and arcade items — hard square pixels, one-pixel dark outline.

| | Background | What they are |
|---|---|---|
| **W1 – W5** | solid **black**, icons in flat **white** | interface glyphs |
| **C1 – C5** | **transparent** (the model returns real alpha: `--transparent`), icons in **full colour** | game items — currency, rewards, gear |

Generate, cut and preview one sheet with `python3 tools/icon_batch.py pixel-retro C1` (Azure); `--all` for the set.
The three load-bearing lines ("one continuous field", "ONE SOLID FILLED shape", "same artist in the same sitting") are explained in tactical-dark/kit/assets/ICON-SHEETS.md — keep them.

## Sheet W1 — Navigation

`home  shop  back  arrow-right  arrow-left  close  check  menu  settings`

```
A 3x3 grid sprite sheet of 9 separate user interface icons for a retro pixel-art mobile game.

ONE SINGLE IMAGE ONLY. Do not produce variations, alternatives, options, or a sheet of different versions to choose from. Do not put the icons on a checkerboard and do not make the background transparent — the background must be a completely opaque, flat, solid BLACK fill covering the whole canvas. One square image, one version, opaque BLACK background.

The whole square image is ONE continuous field of solid pure black (#000000) from edge to edge. Do not draw tiles, cards, panels, frames, circles or boxes behind or around any icon, no line between them — just the 9 symbols floating on one unbroken black field.

Style: retro 8-bit pixel-art UI glyphs. Each icon is ONE SOLID FILLED shape in pure flat white (#FFFFFF) drawn on a coarse pixel grid — every edge is a hard staircase of square pixels, as if the icon were drawn at 16x16 pixels and scaled up with no smoothing. No anti-aliasing, no smooth curves, no line art, no outlines, no gradients, no shading. Every icon is the same visual weight and the same optical size, centred in its own ninth with clear black space around it.

No text, no letters, no numbers. Arrange them as a 3 by 3 grid, evenly spaced.

Row 1: a house (home); a shop with a striped awning; a thick left-pointing arrow with a short tail (back).
Row 2: a thick right-pointing arrow; a thick left-pointing arrow; a bold X (close).
Row 3: a bold check mark; three horizontal bars (menu); a gear with six teeth (settings).
```

## Sheet W2 — Media and sound

`play  pause  restart  refresh  sound  sound-off  music  music-off  video`

```
A 3x3 grid sprite sheet of 9 separate user interface icons for a retro pixel-art mobile game.

ONE SINGLE IMAGE ONLY. Do not produce variations, alternatives, options, or a sheet of different versions to choose from. Do not put the icons on a checkerboard and do not make the background transparent — the background must be a completely opaque, flat, solid BLACK fill covering the whole canvas. One square image, one version, opaque BLACK background.

The whole square image is ONE continuous field of solid pure black (#000000) from edge to edge. Do not draw tiles, cards, panels, frames, circles or boxes behind or around any icon, no line between them — just the 9 symbols floating on one unbroken black field.

Style: retro 8-bit pixel-art UI glyphs. Each icon is ONE SOLID FILLED shape in pure flat white (#FFFFFF) drawn on a coarse pixel grid — every edge is a hard staircase of square pixels, as if the icon were drawn at 16x16 pixels and scaled up with no smoothing. No anti-aliasing, no smooth curves, no line art, no outlines, no gradients, no shading. Every icon is the same visual weight and the same optical size, centred in its own ninth with clear black space around it.

No text, no letters, no numbers. Arrange them as a 3 by 3 grid, evenly spaced.

Row 1: a play triangle; two vertical pause bars; a circular arrow with one arrowhead (restart).
Row 2: two chasing circular arrows (refresh); a speaker with two sound waves; a speaker with a slash across it.
Row 3: a beamed pair of musical notes; the same notes with a slash across them; a video camera with a play triangle on it.
```

## Sheet W3 — Status and system

`warning  alert  info  battery  wifi  trash  hand  eye  search`

```
A 3x3 grid sprite sheet of 9 separate user interface icons for a retro pixel-art mobile game.

ONE SINGLE IMAGE ONLY. Do not produce variations, alternatives, options, or a sheet of different versions to choose from. Do not put the icons on a checkerboard and do not make the background transparent — the background must be a completely opaque, flat, solid BLACK fill covering the whole canvas. One square image, one version, opaque BLACK background.

The whole square image is ONE continuous field of solid pure black (#000000) from edge to edge. Do not draw tiles, cards, panels, frames, circles or boxes behind or around any icon, no line between them — just the 9 symbols floating on one unbroken black field.

Style: retro 8-bit pixel-art UI glyphs. Each icon is ONE SOLID FILLED shape in pure flat white (#FFFFFF) drawn on a coarse pixel grid — every edge is a hard staircase of square pixels, as if the icon were drawn at 16x16 pixels and scaled up with no smoothing. No anti-aliasing, no smooth curves, no line art, no outlines, no gradients, no shading. Every icon is the same visual weight and the same optical size, centred in its own ninth with clear black space around it.

No text, no letters, no numbers. Arrange them as a 3 by 3 grid, evenly spaced.

Row 1: a triangle with an exclamation mark (warning); a bell (alert); a circle with a lowercase i (info).
Row 2: a battery seen from the side with a small cap; three wifi arcs over a dot; a trash can with a lid.
Row 3: a pointing hand, index finger up (tap); an open eye; a magnifying glass.
```

## Sheet W4 — World and tools

`map  radar  compass  flag  pin  wrench  hourglass  clock  calendar`

```
A 3x3 grid sprite sheet of 9 separate user interface icons for a retro pixel-art mobile game.

ONE SINGLE IMAGE ONLY. Do not produce variations, alternatives, options, or a sheet of different versions to choose from. Do not put the icons on a checkerboard and do not make the background transparent — the background must be a completely opaque, flat, solid BLACK fill covering the whole canvas. One square image, one version, opaque BLACK background.

The whole square image is ONE continuous field of solid pure black (#000000) from edge to edge. Do not draw tiles, cards, panels, frames, circles or boxes behind or around any icon, no line between them — just the 9 symbols floating on one unbroken black field.

Style: retro 8-bit pixel-art UI glyphs. Each icon is ONE SOLID FILLED shape in pure flat white (#FFFFFF) drawn on a coarse pixel grid — every edge is a hard staircase of square pixels, as if the icon were drawn at 16x16 pixels and scaled up with no smoothing. No anti-aliasing, no smooth curves, no line art, no outlines, no gradients, no shading. Every icon is the same visual weight and the same optical size, centred in its own ninth with clear black space around it.

No text, no letters, no numbers. Arrange them as a 3 by 3 grid, evenly spaced.

Row 1: a folded map with three panels; a radar screen, a circle with a sweep wedge; a compass rose with four points.
Row 2: a flag on a pole; a map pin, teardrop with a hole; a wrench.
Row 3: an hourglass; a round clock face with two hands; a calendar page with two rings and a grid.
```

## Sheet W5 — Messages, maths, aim

`mail  chat  plus  minus  ring  crosshair  jump  lock  skull`

```
A 3x3 grid sprite sheet of 9 separate user interface icons for a retro pixel-art mobile game.

ONE SINGLE IMAGE ONLY. Do not produce variations, alternatives, options, or a sheet of different versions to choose from. Do not put the icons on a checkerboard and do not make the background transparent — the background must be a completely opaque, flat, solid BLACK fill covering the whole canvas. One square image, one version, opaque BLACK background.

The whole square image is ONE continuous field of solid pure black (#000000) from edge to edge. Do not draw tiles, cards, panels, frames, circles or boxes behind or around any icon, no line between them — just the 9 symbols floating on one unbroken black field.

Style: retro 8-bit pixel-art UI glyphs. Each icon is ONE SOLID FILLED shape in pure flat white (#FFFFFF) drawn on a coarse pixel grid — every edge is a hard staircase of square pixels, as if the icon were drawn at 16x16 pixels and scaled up with no smoothing. No anti-aliasing, no smooth curves, no line art, no outlines, no gradients, no shading. Every icon is the same visual weight and the same optical size, centred in its own ninth with clear black space around it.

No text, no letters, no numbers. Arrange them as a 3 by 3 grid, evenly spaced.

Row 1: a closed envelope; a speech bubble; a bold plus sign.
Row 2: a bold minus sign; a ring with a gem on top; a crosshair, circle with four ticks.
Row 3: a figure leaping upward with arms raised (jump); a padlock; a skull.
```

## Sheet C1 — Currency

`coin  coin-pile  gem  gem-pile  ruby  cash  ticket  crown  clover`

```
A 3x3 grid sprite sheet of 9 separate game item icons for a retro pixel-art mobile game.

ONE SINGLE IMAGE ONLY, on a fully TRANSPARENT background (alpha channel) — no backdrop, no tiles, no cards, no panels, no frames, no shadow on the ground, nothing behind the objects at all. Do not produce variations, alternatives or options, and do not show the same icons twice in different styles. One square image, one version.

Style: 16-bit retro pixel-art game item icons, like a classic console RPG or arcade shop. Each object is drawn on a coarse pixel grid, as if it were 32x32 pixels scaled up with no smoothing: hard square pixels only, no anti-aliasing, no soft gradients, no blur. A one-pixel dark outline (near-black navy) around every shape, flat colour areas with one or two hard-stepped shade tones and a small square highlight on the top-left. A limited bright retro palette. Slight three-quarter view, chunky and readable, filling its cell. Not painterly, not realistic, not smooth vector art.

All 9 must share one identical lighting direction, one outline thickness, one level of detail and one optical size — they are a set from the same game, drawn by the same artist in the same sitting. No text, no letters, no numbers, no logos, no hands, no background scenery. Arrange them as a 3 by 3 grid, evenly spaced, each centred in its own ninth with clear empty space around it.

Row 1: a gold coin seen at a slight tilt with a plain flat face and a thick rim; a small stack of gold coins with two loose coins in front; a blue gem cut like a hexagon seen face on.
Row 2: a small heap of blue gems; a red gem cut like a hexagon, seen face on; a tied leather bag of gold with coins spilling at its mouth.
Row 3: a golden event ticket with a notch cut into each long side; a gold crown with three points set with small red stones; a green four-leaf clover with a short stem.
```

## Sheet C2 — Progress and rewards

`heart  heart-empty  star  star-empty  energy  level-badge  medal  trophy  avatar`

```
A 3x3 grid sprite sheet of 9 separate game item icons for a retro pixel-art mobile game.

ONE SINGLE IMAGE ONLY, on a fully TRANSPARENT background (alpha channel) — no backdrop, no tiles, no cards, no panels, no frames, no shadow on the ground, nothing behind the objects at all. Do not produce variations, alternatives or options, and do not show the same icons twice in different styles. One square image, one version.

Style: 16-bit retro pixel-art game item icons, like a classic console RPG or arcade shop. Each object is drawn on a coarse pixel grid, as if it were 32x32 pixels scaled up with no smoothing: hard square pixels only, no anti-aliasing, no soft gradients, no blur. A one-pixel dark outline (near-black navy) around every shape, flat colour areas with one or two hard-stepped shade tones and a small square highlight on the top-left. A limited bright retro palette. Slight three-quarter view, chunky and readable, filling its cell. Not painterly, not realistic, not smooth vector art.

All 9 must share one identical lighting direction, one outline thickness, one level of detail and one optical size — they are a set from the same game, drawn by the same artist in the same sitting. No text, no letters, no numbers, no logos, no hands, no background scenery. Arrange them as a 3 by 3 grid, evenly spaced, each centred in its own ninth with clear empty space around it.

Row 1: a red heart, plump; the same heart drawn hollow, grey and only outlined with a dark inner shadow; a five-point gold star.
Row 2: the same star hollow, grey and only outlined; a yellow lightning bolt; a blue shield-shaped badge with a gold rim, empty in the middle.
Row 3: a round gold medal on a red ribbon; a gold trophy cup with two handles; a round portrait frame with a hooded adventurer silhouette inside.
```

## Sheet C3 — Items and rewards

`chest  gift  key  bomb  potion  sword  shield  fireball  fire`

```
A 3x3 grid sprite sheet of 9 separate game item icons for a retro pixel-art mobile game.

ONE SINGLE IMAGE ONLY, on a fully TRANSPARENT background (alpha channel) — no backdrop, no tiles, no cards, no panels, no frames, no shadow on the ground, nothing behind the objects at all. Do not produce variations, alternatives or options, and do not show the same icons twice in different styles. One square image, one version.

Style: 16-bit retro pixel-art game item icons, like a classic console RPG or arcade shop. Each object is drawn on a coarse pixel grid, as if it were 32x32 pixels scaled up with no smoothing: hard square pixels only, no anti-aliasing, no soft gradients, no blur. A one-pixel dark outline (near-black navy) around every shape, flat colour areas with one or two hard-stepped shade tones and a small square highlight on the top-left. A limited bright retro palette. Slight three-quarter view, chunky and readable, filling its cell. Not painterly, not realistic, not smooth vector art.

All 9 must share one identical lighting direction, one outline thickness, one level of detail and one optical size — they are a set from the same game, drawn by the same artist in the same sitting. No text, no letters, no numbers, no logos, no hands, no background scenery. Arrange them as a 3 by 3 grid, evenly spaced, each centred in its own ninth with clear empty space around it.

Row 1: a closed wooden treasure chest with steel bands and a lock; a red gift box with a gold ribbon and bow; a brass key with a round bow and two teeth.
Row 2: a round black bomb with a lit fuse; a round glass potion flask with a cork, filled with glowing purple liquid; a steel sword with a gold crossguard and red pommel, pointing up-right.
Row 3: a round wooden shield with a steel rim and a gold boss in the middle; a fireball flying to the right with a flame tail; a campfire flame on two logs.
```

## Sheet C4 — Weapons and gear

`axe  bow  helmet  armor  boots  gem-ring  scroll  spellbook  hammer`

```
A 3x3 grid sprite sheet of 9 separate game item icons for a retro pixel-art mobile game.

ONE SINGLE IMAGE ONLY, on a fully TRANSPARENT background (alpha channel) — no backdrop, no tiles, no cards, no panels, no frames, no shadow on the ground, nothing behind the objects at all. Do not produce variations, alternatives or options, and do not show the same icons twice in different styles. One square image, one version.

Style: 16-bit retro pixel-art game item icons, like a classic console RPG or arcade shop. Each object is drawn on a coarse pixel grid, as if it were 32x32 pixels scaled up with no smoothing: hard square pixels only, no anti-aliasing, no soft gradients, no blur. A one-pixel dark outline (near-black navy) around every shape, flat colour areas with one or two hard-stepped shade tones and a small square highlight on the top-left. A limited bright retro palette. Slight three-quarter view, chunky and readable, filling its cell. Not painterly, not realistic, not smooth vector art.

All 9 must share one identical lighting direction, one outline thickness, one level of detail and one optical size — they are a set from the same game, drawn by the same artist in the same sitting. No text, no letters, no numbers, no logos, no hands, no background scenery. Arrange them as a 3 by 3 grid, evenly spaced, each centred in its own ninth with clear empty space around it.

Row 1: a steel battle axe with a wooden handle; a wooden bow with an arrow nocked; a steel knight helmet with a plume.
Row 2: a steel chest armour plate with gold trim; a pair of brown leather boots with buckles; a gold ring set with a purple gem.
Row 3: a rolled parchment scroll with a red wax seal; a purple spellbook with a gold star on the cover; a war hammer with a steel head and wooden handle.
```

## Sheet C5 — Supplies and places

`potion-red  potion-blue  potion-green  lantern  castle  crystal-ball  meat  rocket  anvil`

```
A 3x3 grid sprite sheet of 9 separate game item icons for a retro pixel-art mobile game.

ONE SINGLE IMAGE ONLY, on a fully TRANSPARENT background (alpha channel) — no backdrop, no tiles, no cards, no panels, no frames, no shadow on the ground, nothing behind the objects at all. Do not produce variations, alternatives or options, and do not show the same icons twice in different styles. One square image, one version.

Style: 16-bit retro pixel-art game item icons, like a classic console RPG or arcade shop. Each object is drawn on a coarse pixel grid, as if it were 32x32 pixels scaled up with no smoothing: hard square pixels only, no anti-aliasing, no soft gradients, no blur. A one-pixel dark outline (near-black navy) around every shape, flat colour areas with one or two hard-stepped shade tones and a small square highlight on the top-left. A limited bright retro palette. Slight three-quarter view, chunky and readable, filling its cell. Not painterly, not realistic, not smooth vector art.

All 9 must share one identical lighting direction, one outline thickness, one level of detail and one optical size — they are a set from the same game, drawn by the same artist in the same sitting. No text, no letters, no numbers, no logos, no hands, no background scenery. Arrange them as a 3 by 3 grid, evenly spaced, each centred in its own ninth with clear empty space around it.

Row 1: a small round flask of red potion with a cork; the same flask with blue potion; the same flask with green potion.
Row 2: a brass lantern with a glowing yellow flame; a small grey stone castle with two towers and a red flag; a glowing crystal ball on a small gold stand.
Row 3: a roasted meat leg on a bone; a red and white festival rocket firework with a stick; a steel anvil on a wooden block.
```
