# Style 2 — "Tactical Dark"

A second skin for the same kit. Same class names, same `sc.js`, same blocks, docs and tests.
Only `core.css` tokens and the component CSS are rewritten.

Direction taken from a dark, flat, neon-outlined survival/shooter GUI (looked at for direction only —
no art, file or screenshot from it is stored in this repo, and none of its assets are reproduced).

## The one-line difference

Current kit: **filled candy plastic** — thick black outline, glossy face, 3D lip, white outlined 3D text.
This style: **dark glass with a lit edge** — near-black fill, thin bright accent border, flat coloured text, soft glow.

## Tokens (`core.css`)

| Token | Super Casual | Tactical Dark |
|---|---|---|
| `--sc-outline` | `#050308` (thick black) | `rgba(120,190,255,.55)` — the border is a *light*, not a black line |
| `--sc-line` | `2.4px` | `1.5px` |
| `--sc-text-stroke` | `.16` | `0` — no outline on text |
| `--sc-text-drop` | `.08` | `0` — no 3D bottom edge |
| `--sc-font` | M PLUS Rounded 1c 900 | a condensed/technical sans, 600–700, uppercase labels, `letter-spacing:.04em` |
| ground | game canvas | `#070B16` page, `#0E1628` panels |

The engine already supports killing the 3D text through those two tokens — that part is free.

## Per-colour variables

Same four-variable contract (`--band --base --line --lip`), different meaning:

- `--base` = the **fill**, a very dark tint of the accent (≈ 12% accent on `#0B1120`)
- `--band` = the top of a subtle vertical gradient (≈ 18%)
- `--line` = the **accent border + text colour**, full brightness
- `--lip` = the **glow**, accent at ~35% alpha, used as `box-shadow: 0 0 10px`

**The trap:** the four variables keep their names but swap jobs. In Super Casual the bright colour is `--base`
(the candy fill). Here the bright colour is **`--line`**. Anything that should read as lit — a progress fill, a
toggle thumb, a label, a border — uses `--line`. `--base`/`--band` are only ever the dark surface *behind*
content. Building a component on `--base` by habit gives you a muddy olive "gold" bar; that happened once.

Accents: electric blue `#3BA7FF`, cyan `#42E8F5`, green `#3BE08A`, olive `#A8C43A`, gold `#F2C14E`,
orange `#F08A3C`, red `#F2495C`, magenta `#E45BD0`, violet `#8C6BFF`, plus muted `#5A6478` for disabled.

## Component notes

- **Button** — flat dark fill, 1.5px accent border, accent text, glow on press instead of a squash.
- **Icon Button** — same, square-ish (radius 10px), icon tinted white or accent.
- **Counter / pill** — translucent dark pill, thin border, white number, small green `+` circle at the end.
- **Progress / Loading** — 10–14px thin bar, flat accent fill with a 1px lighter top line, plus a segmented variant.
- **Popup** — dark panel, thin top-lit border, a title bar with a hairline under it, no ribbon.
- **Tabs / Tab bar** — inactive = dim grey text, active = accent text + a 2px accent underline, no pill.
- **Slot / Shop card** — dark card, thin border, rarity shown by border colour and glow.
- **Joystick / D-pad** — dark hollow ring with a thin accent edge, no gloss on the knob.

## Two of our global rules are actually Super Casual rules

Both must become **per-style** rules, or this style cannot look right:

1. **"Outlined 3D text everywhere."** This style has flat coloured text. Handled by the two tokens above.
2. **"No sharp edges / no clip-path polygons."** Overridden for this style, by the owner, after comparing
   against the pack's own screens. The cut corner is not decoration here — it is the single strongest
   signature of the style, and rounded corners read as a different kit. So in Tactical Dark:
   - the shape is a rectangle with the **top-left and bottom-right corners cut at 45°** (`--cut`), and the
     other two corners *nicked* by 2-3px (`--nick`) rather than left perfectly square;
   - `clip-path: polygon(...)` is allowed and expected;
   - Super Casual is untouched and keeps its rounded corners.

## Anatomy of a button (measured off the reference)

Five layers, in this order:

1. a darker copy of the same shape, offset 4px down-right — drawn with `filter: drop-shadow(4px 4px 0 …)`
   on the host, so it follows the clipped shape automatically instead of being a second element;
2. an outer glow in the button's colour, the second `drop-shadow` in the same filter;
3. the face: a near-flat vertical gradient, 96% → 90% of the accent (not a candy highlight);
4. a thin diagonal slash just inside the bottom-right cut, running parallel to it;
5. bold uppercase label, white on colour, near-black on the light button.

Proportions: `--cut` is 30% of the height, the label is 41% of the height, height 36 / 46 / 58px.
Pressing translates the button 3px down-right onto its own shadow.

## Art

Icons do not carry over — the current 55 are chunky and glossy. This style needs flat, mostly single-colour
glyphs (white or accent), generated as their own sheets. Prompts live in `assets/IMAGE-PROMPTS.md` per style.


---

## Rules that came out of building it

Four of these cost real time to find. They apply to any future style, not just this one.

1. **Contrast before colour.** A label is near-white in every state. Accent-coloured text on a dark panel
   sits near 3:1 and disappears at small sizes. The accent carries *state* — through a border, a thumb, a
   glow, a fill — and the text carries *meaning*, so it stays readable. The toggle was rebuilt twice over
   this.
2. **Every component needs a `:where()` default for `--line`.** The palette only sets `--line` under
   `[data-color]`. Without a default, `color-mix(in srgb, var(--line) …)` is invalid, the whole declaration
   is dropped, and the component silently renders in its OFF/empty state. It bit the toggle and it will bit
   the next one.
3. **Don't build a shape by stacking clipped rectangles.** CSS has no shape primitive: every layer is a box,
   and `clip-path` only masks the painting. Three layers means three polygons that must agree at every
   vertex, and the corner of whichever one disagrees shows through. Either fill the cut corners so the
   silhouette is a plain rounded rectangle (what the button does now), or draw the whole thing as one image.
4. **Port, don't rewrite.** A style is a re-skin. Start every component from the reference file and change
   the paint; never write it from memory. The first pass at this style was written from memory and silently
   dropped about sixty selectors — sizes, `data-pos` anchors, the tutorial's gesture animations, the float's
   `--dx` motion, the star markers' image sizing (which put 160px stars across the progress bar). Nothing
   errors when a selector is missing; the option just does nothing. Two tools now catch it:
   `python3 tools/check_style.py <style>` lists every behavioural selector the style lacks, and
   `--tests` rebuilds the kit's regression pages against the style so the behaviour checks run on it too.
5. **Artwork-dependent numbers are tokens, not constants.** sc.js aimed the Tutorial Hand with a hardcoded
   fingertip position (17% / 5%) that was only true for the Super Casual hand icon. This style's hand has its
   fingertip at 40% / 10%, so the hand pointed beside the target. It is now `--sc-tip-x` / `--sc-tip-y` in
   each style's core.css, measured off that style's `hand.png`.
6. **Read what sc.js actually builds before writing the CSS.** Three components were styled against a DOM I
   assumed: the banner nests its text *inside* `.sc-banner-band`, the timer ring is an **SVG circle** driven
   by `stroke-dashoffset` (and the ring is the *default*, the pill is the variant), and the level badge gets
   an `<img>` of the badge art that has to be hidden when the plate is drawn in CSS.
7. **A block is the real test of a component.** The docs pages passed; the ten blocks still found five things:
   the claimed tick covered the count (this style puts the count bottom-right), labels touched the frame of
   labelled icon tiles (Chakra Petch is wider than Lilita One — the tile now grows with its label), `.sc-panel`
   had lost its layout (selector present, `align-self:stretch` gone), the `dark` button came out maroon (the
   warm fill base shows when the accent is grey), and tab / tab-bar icons were too small and too dim.
   `python3 tools/check_style.py <style> --layout` now lists layout properties a style dropped from a selector
   it does have. Build the blocks early: port them with the reference markup and change only the content.
8. **Never let stylesheet order decide.** When a host restyles a child (`.sc-shopcard > .sc-shopcard-buy`) and the
   child's own file has a rule of equal specificity (`.sc-button[data-size="sm"]`), whichever file loads last
   wins — so the bundle and a hand-linked page look different. Name the child's base class in the host rule
   (`.sc-shopcard > .sc-button.sc-shopcard-buy`). `python3 tools/check_style.py <style> --order` proves it.
9. **No literal colours in component CSS.** Every colour is a theme token or a `color-mix()` step of one
   (`core.css`, THEME TOKENS). Lighter steps of an accent lean to `--sc-ink`, of a surface to `--sc-sheen`,
   darker steps to `--sc-shade` — never `#fff` / `#000`, or a light theme breaks. Black is allowed for shadows only.
   This is what lets `themes/*.css` re-skin the style; see `themes/README.md`.
