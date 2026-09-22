# Icon sheet prompts — Tactical Dark

Ten sheets, nine icons each, 3x3, square image.

| | Background | What they are |
|---|---|---|
| **W1 – W5** | solid **black**, icons in flat **white** | interface glyphs — arrows, settings, sound, warnings, tools |
| **C1 – C5** | solid **white**, icons in **full colour** | game items — currency, weapons, gear, rewards |

Save them as `icons-w1.png` … `icons-w5.png` and `icons-c1.png` … `icons-c5.png`, strip the background,
and send them over. Cutting a sheet into its nine files is one command:

```
python3 tools/sheet_to_icons.py icons-w1.png 3 3 tactical-dark/kit/assets home shop back arrow-right arrow-left close check menu settings
```

**Three lines in these prompts are load-bearing. Don't shorten them.**

1. *"one continuous field of solid …"* — without it the model gives every icon its own tile with gutters
   between them, and the sheet can't be cut. Never write it as "no boxes": naming boxes puts boxes in.
2. *"ONE SOLID FILLED shape … never line art"* (white sheets) — anything with interior structure, like a
   coin or a chest, comes back as an outline otherwise.
3. *"one identical lighting direction … same artist in the same sitting"* (colour sheets) — this is what
   stops nine icons drifting into nine different styles. It is the reason for generating nine at a time
   rather than one by one.

Every prompt opens by asking for ONE image on an opaque background. Leave that paragraph in: without it
the model likes to hand back three or four variants, or a transparent PNG on a checkerboard, and none of
those can be cut.

About one sheet in three still comes back tiled. Generate it again — the prompt is fine, the model is not.

---

## Sheet W1 — Navigation

`home  shop  back  arrow-right  arrow-left  close  check  menu  settings`

```
A 3x3 grid sprite sheet of 9 separate user interface icons for a dark sci-fi survival game HUD.

ONE SINGLE IMAGE ONLY. Do not produce variations, alternatives, options, or a sheet of different versions to choose from. Do not show the same icons twice in different styles. Do not put the icons on a checkerboard, and do not make the background transparent or partly transparent — the background must be a completely opaque, flat, solid BLACK fill covering the whole canvas. One square image, one version, opaque BLACK background.

The whole square image is ONE continuous field of solid pure black (#000000) from edge to edge. The only white anywhere in the image is the 9 icons themselves. Do not draw tiles, cards, panels, cells, circles or boxes behind or around any icon, and do not draw any line between them — just 9 white shapes floating on one unbroken black field.

Each icon is ONE SOLID FILLED pure white (#FFFFFF) shape, like a set of font glyphs cut from a single stencil. Never line art. Never an outlined shape. Never a white outline around a black interior. The white is filled in completely. Black appears inside a shape ONLY where a hole is described below, and such a hole is a simple cut-out, never a thin drawn line.

All 9 must share one identical visual weight, one stroke thickness, one level of detail and one optical size — they are a family drawn by the same hand in the same sitting. Everything is flat and face on: no perspective, no isometric angle, no 3D, no shadow, no gradient, no glow, no text, no letters, no numbers. Arrange them as a 3 by 3 grid, evenly spaced, each centred in its own ninth with clear black space around it.

Row 1: a house with a triangular roof and a small arched doorway cut out of its base; a shop front: one solid block with a scalloped awning across the top and a doorway cut out of the base; a left-pointing arrow: a straight horizontal bar with a triangular head on the left, flat tail on the right.
Row 2: a right-pointing arrow: a straight horizontal bar with a triangular head on the right, flat tail on the left; a left-pointing arrow, slimmer than the back icon, with a longer shaft; an X made of two straight bars of equal thickness crossing at right angles.
Row 3: a tick mark with two straight strokes, the second about twice as long as the first; three straight horizontal bars of equal length, stacked with even gaps; a gear wheel with six square teeth and a round hole cut out of its centre.
```

## Sheet W2 — Media and sound

`play  pause  restart  refresh  sound  sound-off  music  music-off  video`

```
A 3x3 grid sprite sheet of 9 separate user interface icons for a dark sci-fi survival game HUD.

ONE SINGLE IMAGE ONLY. Do not produce variations, alternatives, options, or a sheet of different versions to choose from. Do not show the same icons twice in different styles. Do not put the icons on a checkerboard, and do not make the background transparent or partly transparent — the background must be a completely opaque, flat, solid BLACK fill covering the whole canvas. One square image, one version, opaque BLACK background.

The whole square image is ONE continuous field of solid pure black (#000000) from edge to edge. The only white anywhere in the image is the 9 icons themselves. Do not draw tiles, cards, panels, cells, circles or boxes behind or around any icon, and do not draw any line between them — just 9 white shapes floating on one unbroken black field.

Each icon is ONE SOLID FILLED pure white (#FFFFFF) shape, like a set of font glyphs cut from a single stencil. Never line art. Never an outlined shape. Never a white outline around a black interior. The white is filled in completely. Black appears inside a shape ONLY where a hole is described below, and such a hole is a simple cut-out, never a thin drawn line.

All 9 must share one identical visual weight, one stroke thickness, one level of detail and one optical size — they are a family drawn by the same hand in the same sitting. Everything is flat and face on: no perspective, no isometric angle, no 3D, no shadow, no gradient, no glow, no text, no letters, no numbers. Arrange them as a 3 by 3 grid, evenly spaced, each centred in its own ninth with clear black space around it.

Row 1: a triangle pointing right with very slightly rounded corners; two vertical rounded bars side by side with an even gap; a circular arrow: a ring broken by a gap, with a triangular arrowhead at one end.
Row 2: two curved arrows chasing each other in a circle, each with a triangular head; a speaker cone pointing right with two curved sound waves beside it; the same speaker cone with a small X beside it instead of the waves.
Row 3: a single musical note with a round head and one flag, nothing beside it; the same musical note with a small X beside it; a rounded rectangle with a triangle pointing right cut out of its middle.
```

## Sheet W3 — Status and system

`warning  alert  info  battery  wifi  trash  hand  eye  search`

```
A 3x3 grid sprite sheet of 9 separate user interface icons for a dark sci-fi survival game HUD.

ONE SINGLE IMAGE ONLY. Do not produce variations, alternatives, options, or a sheet of different versions to choose from. Do not show the same icons twice in different styles. Do not put the icons on a checkerboard, and do not make the background transparent or partly transparent — the background must be a completely opaque, flat, solid BLACK fill covering the whole canvas. One square image, one version, opaque BLACK background.

The whole square image is ONE continuous field of solid pure black (#000000) from edge to edge. The only white anywhere in the image is the 9 icons themselves. Do not draw tiles, cards, panels, cells, circles or boxes behind or around any icon, and do not draw any line between them — just 9 white shapes floating on one unbroken black field.

Each icon is ONE SOLID FILLED pure white (#FFFFFF) shape, like a set of font glyphs cut from a single stencil. Never line art. Never an outlined shape. Never a white outline around a black interior. The white is filled in completely. Black appears inside a shape ONLY where a hole is described below, and such a hole is a simple cut-out, never a thin drawn line.

All 9 must share one identical visual weight, one stroke thickness, one level of detail and one optical size — they are a family drawn by the same hand in the same sitting. Everything is flat and face on: no perspective, no isometric angle, no 3D, no shadow, no gradient, no glow, no text, no letters, no numbers. Arrange them as a 3 by 3 grid, evenly spaced, each centred in its own ninth with clear black space around it.

Row 1: a triangle with a round hole and a short slot cut out of its centre to form an exclamation mark; an exclamation mark cut out of a solid disc: a short slot above a round dot; a lowercase letter i cut out of a solid disc: a round dot above a short slot.
Row 2: a battery lying on its side with a small terminal at one end and one slot cut out of its body; three stacked arcs above a round dot; a rubbish bin with a lid and three slots cut out of its body.
Row 3: a hand with the index finger pointing up and the other fingers curled; an eye: a pointed oval with a round hole cut out of its centre; a magnifying glass: a thick ring with a round hole cut out of the middle and a short angled handle at the lower right.
```

## Sheet W4 — World and tools

`map  radar  compass  flag  pin  wrench  hourglass  clock  calendar`

```
A 3x3 grid sprite sheet of 9 separate user interface icons for a dark sci-fi survival game HUD.

ONE SINGLE IMAGE ONLY. Do not produce variations, alternatives, options, or a sheet of different versions to choose from. Do not show the same icons twice in different styles. Do not put the icons on a checkerboard, and do not make the background transparent or partly transparent — the background must be a completely opaque, flat, solid BLACK fill covering the whole canvas. One square image, one version, opaque BLACK background.

The whole square image is ONE continuous field of solid pure black (#000000) from edge to edge. The only white anywhere in the image is the 9 icons themselves. Do not draw tiles, cards, panels, cells, circles or boxes behind or around any icon, and do not draw any line between them — just 9 white shapes floating on one unbroken black field.

Each icon is ONE SOLID FILLED pure white (#FFFFFF) shape, like a set of font glyphs cut from a single stencil. Never line art. Never an outlined shape. Never a white outline around a black interior. The white is filled in completely. Black appears inside a shape ONLY where a hole is described below, and such a hole is a simple cut-out, never a thin drawn line.

All 9 must share one identical visual weight, one stroke thickness, one level of detail and one optical size — they are a family drawn by the same hand in the same sitting. Everything is flat and face on: no perspective, no isometric angle, no 3D, no shadow, no gradient, no glow, no text, no letters, no numbers. Arrange them as a 3 by 3 grid, evenly spaced, each centred in its own ninth with clear black space around it.

Row 1: a folded map with two fold lines cut out; a radar dish seen from the side with three arc marks beside it; a disc with a diamond shaped needle hole cut out of its centre.
Row 2: a triangular flag on a straight pole; a map pin: a teardrop pointing down with a round hole cut out of its wide end; a spanner seen at an angle with an open jaw.
Row 3: an hourglass with a narrow waist and a base at each end; a disc with two slot shaped holes cut out to form the hands; a rounded square with two tabs on top, a line cut out below them and four small square holes cut out beneath.
```

## Sheet W5 — Messages, maths, aim

`mail  chat  plus  minus  ring  crosshair  jump  lock  skull`

```
A 3x3 grid sprite sheet of 9 separate user interface icons for a dark sci-fi survival game HUD.

ONE SINGLE IMAGE ONLY. Do not produce variations, alternatives, options, or a sheet of different versions to choose from. Do not show the same icons twice in different styles. Do not put the icons on a checkerboard, and do not make the background transparent or partly transparent — the background must be a completely opaque, flat, solid BLACK fill covering the whole canvas. One square image, one version, opaque BLACK background.

The whole square image is ONE continuous field of solid pure black (#000000) from edge to edge. The only white anywhere in the image is the 9 icons themselves. Do not draw tiles, cards, panels, cells, circles or boxes behind or around any icon, and do not draw any line between them — just 9 white shapes floating on one unbroken black field.

Each icon is ONE SOLID FILLED pure white (#FFFFFF) shape, like a set of font glyphs cut from a single stencil. Never line art. Never an outlined shape. Never a white outline around a black interior. The white is filled in completely. Black appears inside a shape ONLY where a hole is described below, and such a hole is a simple cut-out, never a thin drawn line.

All 9 must share one identical visual weight, one stroke thickness, one level of detail and one optical size — they are a family drawn by the same hand in the same sitting. Everything is flat and face on: no perspective, no isometric angle, no 3D, no shadow, no gradient, no glow, no text, no letters, no numbers. Arrange them as a 3 by 3 grid, evenly spaced, each centred in its own ninth with clear black space around it.

Row 1: a closed envelope: a rectangle with a wide V cut out of its upper half; a speech bubble: a rounded rectangle with a small tail and three round dots cut out; a plus sign made of two crossing bars of equal thickness.
Row 2: a single horizontal bar; a plain circle with a smaller circle cut out of its centre; a ring with a round hole cut out of the centre and four short bars sticking out at top, bottom, left and right.
Row 3: a thick chevron arrow pointing up with two short motion streaks below it; a closed padlock: a solid body with a round keyhole cut out and a thick shackle arch on top; a skull from the front with two round eye holes and a small nose hole cut out.
```

## Sheet C1 — Currency

`coin  coin-pile  gem  gem-pile  ruby  cash  ticket  crown  clover`

```
A 3x3 grid sprite sheet of 9 separate game item icons for a dark survival shooter.

ONE SINGLE IMAGE ONLY. Do not produce variations, alternatives, options, or a sheet of different versions to choose from. Do not show the same icons twice in different styles. Do not put the icons on a checkerboard, and do not make the background transparent or partly transparent — the background must be a completely opaque, flat, solid WHITE fill covering the whole canvas. One square image, one version, opaque WHITE background.

The whole square image is ONE continuous field of solid pure white (#FFFFFF) from edge to edge. Do not draw tiles, cards, panels, frames, circles or boxes behind or around any icon, no line between them, and no shadow on the ground — just the 9 objects floating on one unbroken white field.

Style: painted game inventory icons for a dark survival shooter. Semi-realistic and chunky, readable at a small size, with soft shading, a clear light source from the top left, gentle highlights and a slightly muted, grubby palette — worn metal, canvas, leather, dulled gold. Each object is drawn face on or at a very slight three-quarter tilt, filling its cell, with no outline stroke around it.

All 9 must share one identical lighting direction, one level of detail, one painting style and one optical size — they are a set from the same game, drawn by the same artist in the same sitting. No text, no letters, no numbers, no logos, no hands holding anything, no background scenery. Arrange them as a 3 by 3 grid, evenly spaced, each centred in its own ninth with clear white space around it.

Row 1: a gold coin seen face on, with a star embossed in the middle; a small pile of gold coins, three stacked and a few loose; a cut blue gem with a flat top, angled shoulders and a pointed bottom.
Row 2: a small pile of blue gems grouped together; a deep red cut gem, narrower and taller than the blue one; a small bundle of green banknotes tied with a paper band.
Row 3: a golden event ticket with a notch cut into each long side; a gold crown with three points set with small red stones; a green four-leaf clover with a short stem.
```

## Sheet C2 — Progress and rewards

`heart  heart-empty  star  star-empty  energy  level-badge  medal  trophy  avatar`

```
A 3x3 grid sprite sheet of 9 separate game item icons for a dark survival shooter.

ONE SINGLE IMAGE ONLY. Do not produce variations, alternatives, options, or a sheet of different versions to choose from. Do not show the same icons twice in different styles. Do not put the icons on a checkerboard, and do not make the background transparent or partly transparent — the background must be a completely opaque, flat, solid WHITE fill covering the whole canvas. One square image, one version, opaque WHITE background.

The whole square image is ONE continuous field of solid pure white (#FFFFFF) from edge to edge. Do not draw tiles, cards, panels, frames, circles or boxes behind or around any icon, no line between them, and no shadow on the ground — just the 9 objects floating on one unbroken white field.

Style: painted game inventory icons for a dark survival shooter. Semi-realistic and chunky, readable at a small size, with soft shading, a clear light source from the top left, gentle highlights and a slightly muted, grubby palette — worn metal, canvas, leather, dulled gold. Each object is drawn face on or at a very slight three-quarter tilt, filling its cell, with no outline stroke around it.

All 9 must share one identical lighting direction, one level of detail, one painting style and one optical size — they are a set from the same game, drawn by the same artist in the same sitting. No text, no letters, no numbers, no logos, no hands holding anything, no background scenery. Arrange them as a 3 by 3 grid, evenly spaced, each centred in its own ninth with clear white space around it.

Row 1: a glossy red heart; the same red heart, drained and grey, its colour gone; a gold five-pointed star.
Row 2: the same star, dull grey and unearned; a yellow lightning bolt with a faint glow; a blue hexagonal badge with a metal rim, blank in the middle.
Row 3: a gold medal hanging from a short red and white ribbon; a gold trophy cup with two handles and a dark base; a blank character portrait bust in grey armour, face in shadow.
```

## Sheet C3 — Items and rewards

`chest  gift  key  bomb  potion  sword  shield  fireball  fire`

```
A 3x3 grid sprite sheet of 9 separate game item icons for a dark survival shooter.

ONE SINGLE IMAGE ONLY. Do not produce variations, alternatives, options, or a sheet of different versions to choose from. Do not show the same icons twice in different styles. Do not put the icons on a checkerboard, and do not make the background transparent or partly transparent — the background must be a completely opaque, flat, solid WHITE fill covering the whole canvas. One square image, one version, opaque WHITE background.

The whole square image is ONE continuous field of solid pure white (#FFFFFF) from edge to edge. Do not draw tiles, cards, panels, frames, circles or boxes behind or around any icon, no line between them, and no shadow on the ground — just the 9 objects floating on one unbroken white field.

Style: painted game inventory icons for a dark survival shooter. Semi-realistic and chunky, readable at a small size, with soft shading, a clear light source from the top left, gentle highlights and a slightly muted, grubby palette — worn metal, canvas, leather, dulled gold. Each object is drawn face on or at a very slight three-quarter tilt, filling its cell, with no outline stroke around it.

All 9 must share one identical lighting direction, one level of detail, one painting style and one optical size — they are a set from the same game, drawn by the same artist in the same sitting. No text, no letters, no numbers, no logos, no hands holding anything, no background scenery. Arrange them as a 3 by 3 grid, evenly spaced, each centred in its own ninth with clear white space around it.

Row 1: a wooden treasure chest with iron bands and a domed lid, closed; a wrapped gift box with a ribbon and a bow; an old brass key with a round bow and two teeth.
Row 2: a black round bomb with a lit fuse; a round glass bottle with a cork and glowing green liquid; a steel sword pointing up with a leather grip and a gold crossguard.
Row 3: a steel shield with a flat top, a pointed bottom and a gold rim; a ball of orange flame; a single orange campfire flame.
```

## Sheet C4 — Combat

`rifle  pistol  knife  grenade  ammo  rocket  vest  helmet  gas-mask`

```
A 3x3 grid sprite sheet of 9 separate game item icons for a dark survival shooter.

ONE SINGLE IMAGE ONLY. Do not produce variations, alternatives, options, or a sheet of different versions to choose from. Do not show the same icons twice in different styles. Do not put the icons on a checkerboard, and do not make the background transparent or partly transparent — the background must be a completely opaque, flat, solid WHITE fill covering the whole canvas. One square image, one version, opaque WHITE background.

The whole square image is ONE continuous field of solid pure white (#FFFFFF) from edge to edge. Do not draw tiles, cards, panels, frames, circles or boxes behind or around any icon, no line between them, and no shadow on the ground — just the 9 objects floating on one unbroken white field.

Style: painted game inventory icons for a dark survival shooter. Semi-realistic and chunky, readable at a small size, with soft shading, a clear light source from the top left, gentle highlights and a slightly muted, grubby palette — worn metal, canvas, leather, dulled gold. Each object is drawn face on or at a very slight three-quarter tilt, filling its cell, with no outline stroke around it.

All 9 must share one identical lighting direction, one level of detail, one painting style and one optical size — they are a set from the same game, drawn by the same artist in the same sitting. No text, no letters, no numbers, no logos, no hands holding anything, no background scenery. Arrange them as a 3 by 3 grid, evenly spaced, each centred in its own ninth with clear white space around it.

Row 1: a modern assault rifle seen from the side, black and grey; a modern handgun seen from the side, black and grey; a combat knife with a black grip and a steel blade, pointing up.
Row 2: a green fragmentation grenade with a steel lever; a single brass rifle cartridge standing upright; a small white and red rocket pointing up with blue flame at the base.
Row 3: a green tactical body armour vest seen from the front; a green military helmet seen from a slight angle; a grey rubber gas mask with round glass eyes and a filter.
```

## Sheet C5 — Survival gear

`medkit  bandage  fuel  food  water  backpack  radio  crystal-ball  flashlight`

```
A 3x3 grid sprite sheet of 9 separate game item icons for a dark survival shooter.

ONE SINGLE IMAGE ONLY. Do not produce variations, alternatives, options, or a sheet of different versions to choose from. Do not show the same icons twice in different styles. Do not put the icons on a checkerboard, and do not make the background transparent or partly transparent — the background must be a completely opaque, flat, solid WHITE fill covering the whole canvas. One square image, one version, opaque WHITE background.

The whole square image is ONE continuous field of solid pure white (#FFFFFF) from edge to edge. Do not draw tiles, cards, panels, frames, circles or boxes behind or around any icon, no line between them, and no shadow on the ground — just the 9 objects floating on one unbroken white field.

Style: painted game inventory icons for a dark survival shooter. Semi-realistic and chunky, readable at a small size, with soft shading, a clear light source from the top left, gentle highlights and a slightly muted, grubby palette — worn metal, canvas, leather, dulled gold. Each object is drawn face on or at a very slight three-quarter tilt, filling its cell, with no outline stroke around it.

All 9 must share one identical lighting direction, one level of detail, one painting style and one optical size — they are a set from the same game, drawn by the same artist in the same sitting. No text, no letters, no numbers, no logos, no hands holding anything, no background scenery. Arrange them as a 3 by 3 grid, evenly spaced, each centred in its own ninth with clear white space around it.

Row 1: a white first aid box with a red cross on the front; a rolled white bandage with a loose end; a red fuel canister with a handle and a spout.
Row 2: a tin can of food with a paper label; a clear plastic water bottle with a blue cap; a green canvas backpack with straps and buckles.
Row 3: a black handheld radio with a short antenna; a glass sphere on a small dark stand, glowing faintly purple; a black and yellow handheld torch, lens facing right.
```
