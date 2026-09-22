# CHANGELOG

Newest first. Format and version rules: see `AGENTS.md` §8 (A = Claude, B = Codex/GPT).

## Clean Flat v0.1.0 — the fifth style, the first light one (not yet published)
- Agent: A (Claude) · Date: 2026-09-23 · local only
- For the widest range of games (puzzle, word, trivia, merge, idle, board, kids, cozy). Ported from Fantasy RPG Casual
  and flattened: light token values, white popup card with a soft shadow, Fredoka titles in the accent colour with a
  short rounded bar, a plain rounded ribbon banner, white knobs, hairline edges in each element's own hue, softer lips.
- Accents: each bright base darkened (hue kept) until a white label reads ≥3:1 on it. Yellow is the exception: a
  bright gold fill with a DARK label, and its glyph turns dark with it (`--sc-glyph-on-button`), so text still
  follows the icon colour. White glyph icons turn dark slate on light surfaces via `--sc-glyph-filter`.
- `check_theme.py`: a dark button label is the outline colour in a dark style and the ink in a light one. Every base
  (5) and example theme (3) passes.
- Owner review: tab bars use COLOURED icons only (new sheet N1: home-color, shop-color, settings-color, map-color,
  mail-color, calendar-color, profile-color, friends-color, quest-color; unselected items calmer, still in colour);
  counter icons sit inside the pill; the "+" is a solid circle concentric with the pill's round end; the badge is a
  solid pill with a white number, a white ring and a soft shadow; the default icon button is solid colour with a
  white glyph. `tools/glyph_list.py` now also keeps white glyphs white on solid icon buttons (all styles regenerated).
- Light surfaces darken toward a new `--sc-surface-shade` (soft grey-blue) instead of `--sc-shade`, so slots, shop
  cards, rows and panels stay light; coloured lips still use `--sc-shade`.
- Icons: 155 via Azure — 90 shared, 17 glyphs, 27 puzzle/casual items, 9 coloured nav icons, 12 packs and gift boxes.
- Checked: all 10 blocks with real icons; every referenced icon exists; selectors clean; load order 0 differ;
  contrast PASS for all five bases and three themes. Local commit before this style: `cba91dc`. Nothing pushed.

## Pixel Retro v0.1.0 — the fourth style (not yet published)
- Agent: A (Claude) · Date: 2026-09-22 · local only
- Chosen for breadth: roguelike, platformer, arcade, idle, retro RPG. Ported from Fantasy RPG Casual (token-driven,
  per-component outlines), then reshaped: every radius 0, a one-pixel notch in each corner via `clip-path:var(--sc-notch)`
  on child-free surfaces (slot / shop card / icon button stay square so attached tags are not cut), flat fills with a
  light pixel row on top and a dark step at the bottom, segmented progress fill, pixel window popup (rim–gap–rim),
  Press Start 2P titles with a hard drop and a dashed rule, hard four-way letter outline.
- Palette Sweetie 16 (GrafxKid, CC0); blue, red and purple lightened until they read 3:1 on the panel.
- Font: Pixelify Sans was tried first and dropped — its 2 and 5 read as 8 at game sizes. Jersey 10 (every digit
  distinct), scaled once in core with `font-size-adjust:.56` because of its short x-height; titles opt out.
- `tools/sheet_to_icons.py`: a small part (<12% of the drawing) is dropped only if it does not touch the drawing AND
  sits in the cell's outer margin — an ember from the neighbouring campfire landed in the sword's cell. The first
  version of the rule also dropped the crosshair's centre dot; dots inside a glyph now stay (re-cut C3, W4, C4, W5).
- Icons: 156 via Azure gpt-image-2.5-sunburst (`tools/icon_batch.py pixel-retro`) — the 90 shared names, 18 retro
  glyphs, 36 retro items (toadstools, crate, barrel, stone brick, slime, bat, ghost, gems ×5…) and 12 pieces of shop
  art (chests closed/open, coin and gem packs). One sheet hit an Azure server error and was retried; two sheets were
  regenerated after their prompts were rewritten as original designs. 63 glyphs registered for the glyph filter.
- Checked: every block at phone size with real icons, chest reveal clicked through; every referenced icon exists;
  selectors clean; load order 0 differ; contrast PASS; bundle built.

## Fantasy RPG Casual v0.1.0 — the third style (not yet published)
- Agent: A (Claude) · Date: 2026-09-22 · local only
- `STYLE.md` from the owner's references: velvet purple ground, thick warm-dark outline shared by icons and
  components, matte fills with a lighter top band, gold Cinzel titles with a line-and-diamond ornament, pennants.
- Built by PORTING Tactical Dark (already token-driven): `core.css` keeps every token and changes the values;
  all 30 component files copied, then five reshaped — button (dark outline, solid accent fill with top band,
  thick bottom edge, dark label on light colours), title (serif, ornament), banner (cloth on a wooden rod with
  silver caps, swallow-tail ends), tag (outlined pill), popup edge. Tutorial fingertip measured off this
  style's hand.png (`--sc-tip-x/y` .41/.07).
- Blocks and the all-components example ported from Tactical Dark with fantasy content (EMBER KEEP, chapters,
  potion / bomb / scroll boosters, Market, Treasure). Docs, registry, Icons page generated by `sync_style.py`.
- Two tokens added to every style so the theme checker can model each base's button honestly:
  `--sc-button-label-mix` (35 in Tactical Dark, 0 here) and `--sc-button-dark-label` (colour names whose label is
  the dark outline colour). `check_theme --base` passes for both styles; the three example themes still pass.
- Second pass, so the style reads as its own rather than a recoloured Tactical Dark: font → Baloo 2 (owner's
  pick; titles stay Cinzel); popup as an ornate riveted plate; toggle, slider, checkbox, progress bar, counter,
  tabs, tab bar and joystick knob redrawn in the chunky outlined language (dark outline, bottom edge, top band,
  cream knobs). Side-by-side against Tactical Dark in `_staging/side-by-side.html`.
- Owner review: "the shadow 3D part does not match the button" and "never use black text — the icons are white".
  Fixed across the style: the underside is now an inset lip in the element's own colour (no black slab), the fill
  is the saturated accent with a soft top light, every label is white with the icon outline (text-stroke,
  paint-order), glyphs on fills get a matching dark edge. `check_theme` learned outlined labels
  (`--sc-label-outline`: a label passes if it clears the fill, or its outline separates it from the fill).
- Owner review 2: letter corners spiked (a text-stroke has mitre joins) → the outline is now built from shadows
  in eight directions, which have round joins; the disabled button is a quiet stone plate with a lilac outlined
  label instead of a muddy grey; a locked slot is a closed tile (item a faint silhouette, tag muted) with an
  outlined lock, and the claimed tick gets the same outline.
- Owner review 3: "the brown stroke around the button is ugly — black or that button's dark colour". Every
  component now derives its outline from its own colour (`--sc-outline` redefined per component as the dark of
  its fill / slate); the warm brown stays only on the icon artwork.
- Owner review 4 (joystick): the brown-purple ring was the neutral outline derived from the lilac edge colour,
  and untouched components still had the icon brown from the core token. `--sc-outline` in core is now a
  near-black cool neutral (#100D1C) that every neutral surface inherits; coloured elements keep the dark of
  their own colour. The icon artwork's brown is no longer a CSS colour anywhere.
- `tools/tests/tutorial.html` now reads the style's `--sc-tip-x/y` tokens and the hand's real size instead of
  Super Casual's 76px / .17 / .05, so the fingertip check runs on every style (it was a false failure on the
  two dark styles before).
- Checked: all 10 blocks at phone size; all-components page; `check_style` selectors + `--layout` (same deliberate
  shape differences as Tactical Dark) + `--order` (0 differ); bundle built. Blocks use only icons that exist.

## Fantasy RPG Casual — icons (style 3, started; not yet published)
- Agent: A (Claude) · Date: 2026-09-22 · local only
- Third style, from the owner's reference images in `references/Fantasy RPG Casual/` (gitignored — look at, never
  publish). Icons first: 90 icons in `fantasy-rpg-casual/kit/assets/`, same names as the other styles so games stay
  switchable (fantasy gear where the survival kit had rifles: axe, bow, armor, boots, gem-ring, scroll, spellbook,
  hammer, potions, lantern, castle, meat, anvil). `ICON-SHEETS.md` (10 prompts), `IMAGE-PROMPTS.md`, `offsets.css`.
- Generated with Azure OpenAI gpt-image-2.5-sunburst, added as `--backend azure` in `tools/gen_image.py` (key and
  endpoint in tools/.env, never printed; tolerant of pasted-URL typos; 3 retries on dropped sockets). Every sheet is
  3x3; the model's text-and-image quality made nine of ten sheets usable on the first try.
- `tools/icon_batch.py <style> <SHEET|--all>`: generate → check (one background field to every edge, nine cells each
  holding one centred drawing, clear gutters) → cut (glyphs: brightness→alpha; items: background flood-filled from the
  edges, colours kept) → contact sheet on the kit tile at 1x and 2x for approval. A bad sheet is regenerated, max 3.
  The reference images were described in words; they were never sent to the model.
- Colour sheets are generated with `background: transparent` (`gen_image.py --transparent`): the model returns a real
  alpha channel, so enclosed holes (key bow, bow string, trophy handles, ring) are see-through and highlights are kept.
  The first cut used an edge flood fill, which left those holes white; those icons are kept in
  `_staging/icons/fantasy-rpg-casual/cut-v1/` for comparison only.
- Extension set done (background run, `--all --skip-done`): 302 more glyphs (34 sheets), 90 more items (10),
  36 pieces of shop art — chests in three states, gem packs, gold packs, pennants (6 sheets at 1536x1024,
  320px canvas). 518 icons in the folder. One false rejection (gold packs: big art fills >62% of a cell) →
  the "nearly full" threshold is now 80%. Brand logos from the reference sheet were left out on purpose.

## Custom themes v0.1 — a token file turns Tactical Dark into a different game (not yet published)
- Agent: A (Claude) · Date: 2026-09-19 · local only
- Why: players who like neither ready-made style get "Custom". Pixelfork AI (Astra) writes the look, but the
  game must stay switchable to any ready-made style afterwards. So Custom = a THEME: one `:root` block of
  tokens loaded after a base style. Same HTML, same sc.js, same components.
- Tactical Dark moved onto tokens: ~300 hardcoded colours → 8 surface/text tokens, 13 accents (one value per
  colour name; fills, glows and tinted text are derived with color-mix), button tint/label/fill, and shape and
  type knobs (`--sc-round`, `--sc-cut`, `--sc-spine`, `--sc-glow`, `--sc-caps`, `--sc-tracking`, `--sc-weight`).
  Done by `tools/tokenize_style.py` (nearest token + a color-mix step, so the look is kept). Before/after on
  879 boxes: no size change; the only colour shifts are two "bright accent" borders moving ≤24/255.
- Light themes needed five more tokens, found by building one: `--sc-sheen`, `--sc-shade`, `--sc-scrim`,
  `--sc-glyph-filter`, `--sc-glyph-on-button`. `tools/glyph_list.py` finds the 45 white glyph icons and writes
  the one rule that lets a theme darken them without touching the painted colour icons.
- `themes/README.md` — the contract for Astra: the two rules that keep a game switchable, the token table, limits.
- `tools/check_theme.py` — tokens only, ranges, loaded font weight, and 59 contrast pairs computed the way the
  browser mixes them (text on five surfaces 7:1, accents 3:1, button label per colour). A deliberately bad
  theme fails 16 ways; the base passes.
- Examples, all PASS: `neon-arcade` (pills, heavy glow), `desert-ops` (square, matte, condensed), `daylight`
  (a light theme on a dark base). `themes/preview.html` shows the same ten blocks under each, switched live.
- Verified: theme on the real bundle (`dist/kit.css` + `theme.css`); `check_style` selectors clean; `--order`
  0 differ; blocks' glue colours moved to tokens. Super Casual untouched and NOT themable yet.

## Tools — build_kit.py bundles any style (not yet published)
- Agent: A (Claude) · Date: 2026-09-19 · local only
- `python3 tools/build_kit.py [style]` / `--all`. No argument still builds super-casual, so nothing that calls
  it breaks. Every bundle has the same file names (`kit.css`, `kit.js`, `assets/`, `registry.json`), so a game
  changes style by swapping the folder. `kit.js` is always built from `super-casual/kit/sc.js`, the one runtime.
  A partly skinned style builds with what it has and says what was left out. Only super-casual refreshes the
  game template (`--template` to build it from another style).
- Built `tactical-dark/dist/` (83 KB css, 90 icons). Verified as a drop-in: the Shop block running on
  `dist/kit.css` + `dist/kit.js` only — icons resolve to `dist/assets/`, font loads, no console errors.
- Super Casual bundle: `kit.css` byte-identical; `kit.js` differs only by the fingertip-token change already
  made to sc.js in Tactical Dark v0.1.1.
- Found by comparing the bundle with separately linked files: two Tactical Dark rules tied on specificity with
  another file, so the result depended on load order (shop card buy button 33 vs 37px, its tag 10 vs 11px).
  Fixed by strengthening the host rule. New permanent check: `tools/check_style.py <style> --order` renders
  every component from the bundle and from the component files in reverse order and diffs 293 elements.
  Both styles: 0 differ.

## Tactical Dark v0.2.0 — the ten blocks (not yet published)
- Agent: A (Claude) · Date: 2026-09-19 · local only
- Added `tactical-dark/kit/blocks/`: hud, success, fail, pause, start, reward, daily, settings, shop, loading.
  Ported from the Super Casual blocks — identical markup, glue and wiring — with survival-theme content
  ("LAST SIGNAL", sectors, medkit / grenade / ammo boosters, Armory, Supply Drop) and dark stand-in games.
  `preview.html`, `preview.js` and the blocks README are generated by `tools/sync_style.py`, which now links
  a style's blocks and examples in the sidebar when the files exist instead of always greying them out.
- Fixed while building them (all in Tactical Dark CSS): claimed slot tick moved to the centre so it no longer
  covers the count; labelled icon tiles grow with the label; flat icon tiles show the item at 66%;
  `.sc-panel` stretches and lays out its content again; `dark` buttons are neutral slate with a pale label;
  tab icons 20/24/28px and inactive icons brighter (tabs .7, tab bar .62).
- `tools/check_style.py --layout`: lists layout properties dropped from selectors the style does have.
- Checked: every block opened at phone size; pause popup, claim, chest reveal, daily, tab switching,
  buy → toast and the loading → deploy flow exercised; no console errors. Super Casual untouched.

## Tactical Dark v0.1.1 — full audit: ~60 dropped options restored, tutorial aim fixed (not yet published)
- Agent: A (Claude) · Date: 2026-09-19 · local only
- Why: the owner reported that some components were not working. They were right. The 18 components added in
  v0.1.0 were written from memory instead of ported from the reference files, and about sixty behavioural
  selectors never made it across. Nothing errors when a selector is missing — the option simply does nothing.
- Found by two new checks, both now in `tools/check_style.py`: a selector-coverage diff against the reference
  style, and the kit's own regression pages rebuilt to load the new style's CSS.
- Restored / fixed:
  - **Hint** used an invented `data-at`; the kit uses `data-pos`. All four positions, `data-size`, the
    `--ax/--ay` pointer placement and floating bubbles ported.
  - **Toast** layers use `data-pos`; the `reward` kind and the bottom-entry animation were missing.
  - **Tutorial Hand** was structurally wrong (a blocker covered the whole screen; no gestures). Ported, and
    the fingertip is now aimed from `--sc-tip-x/y` tokens — sc.js hardcoded the Super Casual hand's fingertip
    (17%/5%), this style's is at 40%/10%. Verified: fingertip lands on the target centre to the pixel.
  - **Floating Text** lost its `translate(-50%, …)` centring and `--dx`/`--rot` motion; sizes and `pop` style.
  - **Tag** attached positions (`top-left`, `top-right`, `top`), sizes, tilt. Rebuilt like the button: a real
    border plus two corner gradients, one element.
  - **Stars** arc layout, `--d` stagger, `data-animate`. **Progress** star markers were unsized (160px stars
    over the bar). **Slider** sizes, icon, and the half-thumb maths that keeps the thumb inside the bar.
    **Checkbox** sizes and the tick's scale-in. **Alert** had element and modifier reversed; `dot` kind,
    tab-bar anchoring. **Level** sizes and the XP-bar integration. **Timer** pill icon and warn pulse.
    **Icon Button**: `flat` means neutral-and-bordered, not borderless; round shape and labels on every
    variant. **Counter / Slot** bump animations. **D-pad** arrows at the arm tips. **Shop Card / Top Bar /
    Loading / Banner** layouts ported.
- sc.js: one shared change — the tutorial fingertip reads `--sc-tip-x` / `--sc-tip-y`, defaulting to the old
  values. Super Casual suite re-run: 19 pages, 0 failed.
- Tested: `check_style.py` — every behavioural selector covered, 9 reviewed exceptions recorded with reasons
  in `tactical-dark/style-check.json`. Regression pages against Tactical Dark — all behaviour checks pass; the
  remaining failures assert Super Casual's own pixel sizes, hex colours and ribbon tails. Every docs page
  reviewed by eye in a grid (`_staging/docs-review.html`).

## Tactical Dark v0.1.0 — a complete second style (not yet published)
- Agent: A (Claude) · Date: 2026-09-19 · **local only, nothing committed** at the owner's request
- Done: A second style built from the owner's reference screens of a dark survival GUI pack. All 30
  components, 90 icons, its own docs site. `sc.js` is untouched and shared — every component keeps the same
  class names, attributes and events, so the docs pages are portable between styles with no edits.
- Structure mirrors `super-casual/kit` exactly (`core.css`, `sc.js`, `components/<n>/<n>.css` + `.md`,
  `docs/`, `assets/`, `registry.json`, `blocks/`, `examples/`). That is what makes the docs portable:
  every page loads `../core.css` and `../components/x/x.css`, so the same HTML renders whichever style it
  sits in.
- Icons: 90, generated from 10 sheets of 9. The split matters — 45 flat white glyphs for interface, 45
  painted colour items for things in the game. Generating nine at a time is what keeps them a family;
  the first attempt made them one at a time and a quarter of the set drifted.
- The button was rebuilt four times before it was right, and the honest reason is in STYLE.md: CSS has no
  shape primitive, so stacking clipped rectangles always leaks a corner somewhere. Filling the cut corners
  instead of cutting them away removed the whole class of bug and let the final version be one element
  with a real border and two gradients.
- Tested: every component rendered and checked at real size; no broken images; no console errors.
- Notes for next agent: `tools/build_kit.py` still only knows about Super Casual. It needs a style argument
  before Tactical Dark can ship on the CDN.

## v0.44.1-A — Flat knob, clean press shading, steady debug line
- Agent: A (Claude) · Date: 2026-09-16
- Fixed, all three from the owner's screenshots:
  - **The moving knob is flat now.** Dropped its 3D depth: the dark bottom lip (`inset 0 -12% var(--lip)`) and the drop shadow are gone, leaving a simple top-lit ball. Same for the ghost knob.
  - **The press no longer draws a rectangle.** The arm's shading ran the full half-length of the bar, so it crossed the middle square as a hard-edged box. Each arm's gloss and press gradient now fade out exactly where the middle square starts (`--reach: 100% - thick/arm * 100%`), so the shading covers only the arm that sticks out. This also cleans up the unpressed pad, where four overlapping glosses used to tint the centre.
  - **The readout no longer pushes the controls sideways.** The docs preview is a centred flex row, so the `<p class="log">` was sitting beside the controls and every text change moved them. It is now a full-width line of its own (`flex:0 0 100%`) with a `min-height`, under the controls. Same fix on the Action Buttons page.
- Tested: `tools/tests/controls.html` 26/26. Checked the pressed pad and the flat knob at 180px.

## v0.44.0-A — D-pad is one shape, arrow-free and ghost sticks, readable action labels
- Agent: A (Claude) · Date: 2026-09-16
- Done, all from the owner's review of the controls:
  - **The D-pad is now one continuous plus**, not four bars stuck together. It is drawn as two layers — a dark plus (the outline) and a coloured plus on top — built from the same pair of crossing bars, plus a small centre patch that fills the four inner corners. One colour across the whole shape, rounded tips, square inner corners (they meet another part of the same shape).
  - **Arrows moved onto the arms**, at the end of each one, instead of sitting on the dark base.
  - **Press animation:** the pressed arm sinks slightly towards the middle and loses its gloss (`.sc-joystick-arm.sc-on`). Small on purpose. The whole shape stays unbroken.
  - **`data-arrows="false"`** — a clean stick or a clean pad with no arrows.
  - **`data-knob="ghost"`** — grey, half see-through middle, for a stick that should not cover the game.
- Fixed (the owner's second screenshot): action button labels were tiny and far from the icon. The label is now pinned just above the bottom of the circle, right under a slightly smaller icon, starts at 26% of the button size, and never shrinks below the kit's readable minimum (10px) — the old shrink-to-fit could take it down to 55%, which on a small button meant 8px. Its box is also no longer stretched to the button's width, which had knocked the 3D copy out of line.
- Tested: `tools/tests/controls.html` 26/26 (new checks: one-plus markup, pressed arm marked, arrows hidden, ghost knob). Full runner 17/19 — `toast` and `loading` failed on wall-clock assertions while this browser was throttling timers ~15× (a 40 ms timer took 620 ms); both pass at normal speed, and neither page touches anything changed here. The runner's per-page timeout is now 90s for the same reason.
- Notes for next agent: the D-pad's shape lives in `joystick.css` only — `.sc-joystick-cross` (+ `::before`, `::after`) is the dark layer and the corner patch, `.sc-joystick-fill` (+ `::before`) the coloured one. Keep both layers built from the same two bars, or the outline will not line up.

## v0.43.1-A — Action icons (icons5) + labels that fit the round button
- Agent: A (Claude) · Date: 2026-09-16
- Done: The owner delivered the action-icon sheet. Cut into 8 kit icons: `sword`, `shield`, `fireball`, `jump`, `bomb`, `rocket`, `crosshair`, `potion` (56 icons total). Optical offsets regenerated, names added to `registry.json → icons.names` and to the icon list in `AI-GUIDE.md`; the Action Buttons docs and the controls example now use them.
- Fixed: a long label on a round Action Button crossed the button's edge ("Jump" on a 92px button). `markLong` now measures the button as a circle — the chord at the label's lowest line, minus the border and the text outline — and shrinks the label to fit (min 55%). Same shrink-to-fit idea as the tab labels; no ellipsis on outlined text.
- Fixed: the controls example kept the player where it was when the screen size changed, instead of leaving it stuck in a corner.
- Tested: 19 test pages, 0 failed. Checked the example at 375×812: both labels sit inside their buttons, no broken images.
- Notes for next agent: icon sheets go to `icons/` (gitignored source), cropped PNGs to `super-casual/kit/assets/`, then `tools/icon_offsets.py` and `registry.json → icons.names`, then rebuild dist.

## v0.43.0-A — Movement controls: Joystick / D-Pad + Action Buttons
- Agent: A (Claude) · Date: 2026-09-16
- Done: Two new components, in the kit style (rounded, outlined, glossy — no polygons, no code-drawn art):
  - **Joystick / D-Pad** `.sc-joystick` (component 29). `data-type="stick|dpad"`, `data-snap="free|8|4"`, `data-mode="fixed|follow"` (follow = invisible zone, the pad appears under the thumb and hides on release), `data-size="sm|md|lg"`, `data-keys="false"` to switch keyboard off. Fires `move` (`{x, y, angle, distance, dir}`) while held and `end` on release; `SC.joystick.get(el)` reads the current vector. Touch, mouse and WASD/arrow keys, diagonals included. Direction arrows light up; the knob is clamped inside the base, and in follow mode the whole pad is clamped inside its zone.
  - **Action Buttons** `.sc-actions` + `button.sc-action` (component 30). `data-layout="cluster|row|column|grid"`, sizes sm/md/lg, `data-icon`/text/`data-badge`, disabled state. Fires `press` and `release` on the group with `detail.value`, so a game can hold-to-charge.
  - Docs pages, AI manuals (`joystick.md`, `actions.md`), registry entries (31 items) and `examples/controls-on-canvas.html` (both pads + an action cluster over a live canvas).
  - CDN tag bumped to v0.43.0-A. Dist rebuilt.
- Tested: New `tools/tests/controls.html` (22 checks: parts built, drag + clamp + release, arrow highlight, snap 8/4, follow show/hide/clamp, keyboard diagonal, `data-keys="false"`, action press/release, disabled silence, dynamic insert, no observer churn). Full runner: **19 pages, 0 failed**.
- Notes for next agent: Test pages that measure geometry must disable animations (`* { animation:none !important; transition:none !important; }`) — browsers freeze animations and rAF in hidden/background iframes, which is how the runner loads them. `settle()` helpers use `setTimeout`, never `requestAnimationFrame`, for the same reason.

## v0.42.0-A — Responsive fixes: popups fit short screens, readable minimum text
- Agent: A (Claude) · Date: 2026-09-16
- Done: The owner asked if everything is fully responsive. A sweep of all 10 blocks × 10 screen sizes (320×568 … iPad Pro 13", phone landscape, desktop) found 22 problems: popups cut off on short phones (Settings on 4 sizes, Pause, Daily) and text below 9px on small phones/landscape (Shop even on Galaxy S26). Fixes:
  - **Popup** now scales like the Screen Shell: `fitPopup()` in `sc.js` sets `--sc-pop-s = min(vw/400, vh/870, fit width, fit height)` on open, on resize and when the box changes size.
  - The box is a fixed 330px design width, centered with `place-content: unsafe center` so a too-tall box scales around the screen center. Popup padding respects safe areas.
  - **Readable minimum text:** `core.css` has `--sc-min-text: 10px`. `.sc-text` uses `--sc-fs = max(--fs, --sc-min-fs)` for size, outline and 3D edge. Screen Shell sets `--sc-min-fs = 10px / scale` and Popup `10px / popup scale`. Shop card bonus text follows.
  - Start block: more spacing between side shortcuts. Docs inline popups keep `width:min(330px,100%)`.
  - Added `tools/tests/responsive.html` (the sweep, ~3 min, not in index.html). CDN tag bumped to v0.42.0-A. Dist rebuilt.
- Tested: `tools/tests/responsive.html` 100/100 OK (no page scroll, nothing off-screen, no text under 9 real px). Visual check of Settings popup, Shop and Start at 320×568. All 18 component test pages pass.
- Notes for next agent: `font-size` on `.sc-text` is now `!important`. Change `--fs`, never `font-size`, on outlined text. Landscape still shrinks to ~46% (portrait-first kit).

## v0.41.1-A — Public repo + no-install AI guide
- Agent: A (Claude) · Date: 2026-09-15
- Done: At the owner's request, the repo is public again and GitHub Pages is re-enabled (`.nojekyll` added). Games can use the kit with zero install via jsDelivr: `…/gh/advme/mobile-game-ui-library@v0.41.1-A/super-casual/dist/kit.css` + `kit.js` (icons resolve next to kit.js automatically). Added:
  - `AI-GUIDE.md`: one page for Pixelfork or any AI, with the 2 lines, page pattern, SC API, component table generated from the registry, blocks with live links, icons, and rules.
  - `llms.txt`: short pointer file.
  - `templates/cdn-game.html`: the full mini game loading the kit from the CDN.
  - README rewritten for users; `registry.json → cdn`; index links; STATUS/AGENTS note to update the pinned tag on each release.
- Tested: Checked the repo for secrets before going public (none; history contains only the owner's commit name/email). After push: CDN kit.css/kit.js/icons and the Pages example game loaded (see next check).
- Notes for next agent: The CDN is pinned to a tag on purpose (stable for games). `@main` also works, but jsDelivr caches it for up to 12 h.

## v0.41.0-A — Device preview for blocks (desktop) + simulated safe areas
- Agent: A (Claude) · Date: 2026-09-15
- Done: At the owner's request, opening a block on a desktop now shows it in `kit/blocks/preview.html`:
  - Device buttons: Desktop · Phones (iPhone 17 Pro, iPhone 17 Pro Max, Google Pixel 10 Pro, Samsung Galaxy S26, Galaxy S26 Ultra, iPhone SE) · Tablets (iPad Air 11", iPad Pro 13", Galaxy Tab S10), plus Rotate.
  - A "Safe areas" toggle simulates the notch/island and home bar.
  - A block picker (from the registry), scale-to-fit, CSS-drawn frames (Dynamic Island, punch-hole, home indicator), an "Open full page" link, and a URL + localStorage that remember the choice.
  - Phones/tablets (touch, no hover) skip the viewer and open the block full screen; `preview.html` itself redirects them to the block.
  - Each block loads a tiny docs-only `blocks/preview.js`.
  - Kit change: `core.css` defines `--sc-safe-top/right/bottom/left` from `env()`; Screen Shell, Tab Bar and Toast use these variables, so the viewer can simulate device safe areas. Dist rebuilt.
- Tested: On desktop, `start.html` redirects to the viewer. iPhone 17 Pro portrait shows the top bar below the island and the tab bar above the home indicator. Rotate works, as do Pixel 10 Pro (punch-hole), iPad Air and Desktop (full width, rotate disabled). At mobile emulation, blocks open directly and `preview.html` redirects to the block. All 18 test pages pass.
- Notes for next agent: After the desktop→viewer redirect, Chrome can hand the iframe half-cancelled stylesheet requests. The viewer reloads the frame once if any stylesheet is missing. The kit is portrait-first: in phone landscape the 400×870 design scales down a lot (a possible future "landscape layout" task). Device viewport sizes are close approximations.

## v0.40.0-A — One-file bundle + Pixelfork game template
- Agent: A (Claude) · Date: 2026-09-15
- Done:
  - Added `tools/build_kit.py`, which builds `super-casual/dist/`: `kit.css` (core + all 28 component CSS in a safe order, 93 KB), `kit.js` (runtime), `assets/` (icons, offsets, IMAGE-PROMPTS.md), `registry.json` and a README. It also copies dist into the template. It fails loudly if a new component is missing from its ORDER list.
  - Added `templates/pixelfork-game/`: a complete mobile game using only the bundle, with Loading → Start (Top Bar, settings) → HUD (pause, star score bar, coins, timer) → Pause popup (sound/music) → Success (stars, coin reward) / Fail (progress, retry) → Home. It has a CONFIG block (title, time, target, rewards, image re-theming), localStorage save, a UI controller, and a stand-in tap-the-balls game behind a clear `Game`/`UI` contract to replace with a real engine. Includes `AI.md` with instructions for Pixelfork's AI.
  - Kit: added `SC.timer.left(el)`.
  - AGENTS.md now lists dist, template and build step (run the build after any kit change), and Installation docs mention the bundle/template.
- Tested: At 375×812, loading → start; Play → HUD with 30 s timer; Pause freezes the timer and Resume continues; a real tap on a ball scores; win gives 3 stars and 150 coins, saved as level 2; Next → HUD; lose → Fail; Home shows Level 2 and 150 coins.
- Notes for next agent: `templates/pixelfork-game/kit/` is gitignored (built copy). Run `python3 tools/build_kit.py` before opening the template. `super-casual/dist/` IS committed, so always rebuild it before publishing.

## v0.39.0-A — Custom images everywhere + image prompt templates
- Agent: A (Claude) · Date: 2026-09-15
- Done: The owner asked whether AIs can change the pictures inside components. Now they can, in three ways:
  - Every icon attribute (`data-icon` on buttons, icon buttons, counters, slots, progress, tabs, tab bar, shop cards, row avatar/score, loading; `data-avatar` on Top Bar; `icon` in `SC.toast`/`SC.float`) accepts a kit name, a relative path, a web address or a `data:` image, via one resolver `iconSrc()` in `sc.js`.
  - `SC.setImage(name, src)` replaces a picture for the whole page, including already-rendered ones and the built-ins (check, lock, alert, level-badge, hand, avatar, star, star-empty). `SC.setImage(name, null)` resets.
  - `SC.icon(nameOrPath)` returns the resolved URL; custom images get `data-custom`.
  - Added `kit/assets/IMAGE-PROMPTS.md`: a mandatory style block, one-icon and sheet templates, a ready-made subjects table and after-generation steps (crop, where to save, how to use). Added a `docs/images.html` page (in NAV), and updated `registry.json → icons.note`, AGENTS.md and the Introduction.
- Tested: New `tools/tests/images.html` 17/17 (name, relative path, full URL, data: image loading; alias still mirrors; slot/shop card/top bar/row avatar/toast with paths; SC.icon; SC.setImage on built-ins and icons, existing and new elements, reset). All 18 test pages pass.
- Notes for next agent: A value counts as a path if it contains `/`, `.` or `:`; kit icon names must stay plain kebab-case. Offsets (optical centering) only exist for kit assets.

## v0.38.5-A — Hint Bubble: pointer never covers text, side pointers fit the shape
- Agent: A (Claude) · Date: 2026-09-15
- Done: The owner reported that (1) a top/bottom pointer covered letters and (2) left/right pointers looked like separate pieces. Fixes:
  - The bubble is now `isolation:isolate` and both pointer squares are `z-index:-1`, so they draw over the outline but under the text.
  - Side pointers are narrower (13px, sm 10px), and side bubbles get `min-height: 3×font` so the pointer base always sits on the straight edge instead of the rounded corners.
  - Floating bubbles measure `--ax/--ay` inside the border (they were one outline width off) and keep the pointer away from the corners.
  - Scaling inside a Screen Shell now uses `--hint-s` instead of overwriting `--arrow`.
- Tested: 3× zoom of top, bottom, left, right and small (continuous outline, text uncovered); docs tap-to-show at normal scale. `tools/tests/hint.html` 16/16 (new check: pointer behind text); `tutorial.html` 14/14.
- Notes for next agent: Pointer size variables: `--arrow` (square side, uses `--hint-s`), `--ah`, `--ad`. Side pointers need the bubble's straight edge ≥ pointer base, which is why side bubbles have the min-height.

## v0.38.4-A — Hint Bubble: flat (no 3D shade)
- Agent: A (Claude) · Date: 2026-09-15
- Done: At the owner's request, removed the grey bottom shade band (`inset 0 -3px #d9dff0`) from the Hint Bubble and its matching gradient in the bottom pointer. Bubbles are now flat white with the dark outline. Pointer geometry (continuous outline) is unchanged.
- Tested: All 4 pointer directions + small size at 2.2× zoom. `tools/tests/hint.html` 15/15.
- Notes for next agent: The owner prefers hint bubbles flat. Don't add 3D shading back to them.

## v0.38.3-A — Tabs: long labels no longer cut in half
- Agent: A (Claude) · Date: 2026-09-15
- Done: The owner reported tab labels like "Chests"/"Inbox" showing "Ch…" with the dark outline copy still full, so the text looked broken. Removed `overflow:hidden; text-overflow:ellipsis` from `.sc-tab > .sc-text`. `markLong` in `sc.js` now fits tab labels: it measures the room and shrinks the label (`--fs`) so the whole word fits. If it would go below 60% it hides the tab icon (`.sc-tab-tight`) and refits, never below 50%. It runs when tabs build/change, on resize and after fonts load.
- Tested: Docs at desktop width ("Chests" 19→14.8px, "Inbox" with badge full) and at 375×812 (all labels whole). New check in `tools/tests/tabs.html` (3 icon tabs in 240px: labels fit, no ellipsis) passes 25/25. All 17 test pages pass.
- Notes for next agent: This was the last `text-overflow: ellipsis` on outlined text in the kit (the AGENTS.md rule already forbids it). For other long labels use the `.sc-long` fade pattern or this shrink-to-fit pattern.

## v0.38.2-A — Hint Bubble: continuous pointer outline
- Agent: A (Claude) · Date: 2026-09-15
- Done: The owner reported that the Hint Bubble's pointer broke the outline where it meets the bubble (white wedges cut the border). The pointer is now two rotated rounded squares: a dark one half an outline below the bubble's inner border edge, and a same-size white one an outline width further in. The dark edges now flow straight out of the bubble border with the same thickness and no gaps or bumps, in all 4 directions. The bottom pointer continues the grey shade band via a diagonal gradient. The pointer is a bit bigger (17px, sm 13px).
- Tested: 10× zoom of the joint (no gap, no bump, shade band continuous) and all 4 directions + small size at normal scale. `tools/tests/hint.html` 15/15.
- Notes for next agent: Pointer geometry uses `--arrow` (square side), `--ah` (half diagonal) and `--ad` (outline × √2). Keep the two squares the same size; the offset between them equals `--ad`.

## v0.38.1-A — Docs: Introduction and Installation
- Agent: A (Claude) · Date: 2026-09-15
- Done: Added `docs/introduction.html` (what the kit is, the look, a step-by-step guide for AI agents, tables of all components and blocks generated from the registry) and `docs/installation.html` (folder layout, page setup, minimal game page, how components work, Screen Shell basics, local preview). New `SCDocs.article()` renders prose pages. Both are enabled in the NAV, and the root `index.html` + README point to Introduction and the test runner.
- Tested: Both pages render in the browser with the NAV active and code blocks with Copy.
- Notes for next agent: In docs pages, a literal `</script>` inside code samples must be written `<\/script>` or it ends the page script.

## v0.38.0-A — Loading block
- Agent: A (Claude) · Date: 2026-09-15
- Done: Added `kit/blocks/loading.html`, the start-up flow. A solid Screen Shell with the gold game title and `.sc-loading` (bouncing coin, rotating tips) runs simulated asset loading via `SC.loading.set(loaded/total)`. On `done` the bar hides and PLAY + a blinking "Tap to start" appear; PLAY hides the loading screen and shows the game HUD. This completes all 10 planned blocks. `blocks/README.md` now notes that custom wrappers hidden with `hidden` need a `[hidden]` glue rule.
- Tested: Opened at 375×812. Loading shows only the bar (PLAY hidden) and counts to 100%. Then the bar hides and PLAY shows, and PLAY switches to the HUD. No scroll.
- Notes for next agent: All 10 blocks are in `kit/blocks/` and listed in `registry.json → blocks` and the docs NAV "Blocks" group.

## v0.37.0-A — Shop block
- Agent: A (Claude) · Date: 2026-09-15
- Done: Added `kit/blocks/shop.html`, a solid shop screen. It has a back button + coin/gem counters, a `SHOP` title (md), a purple Item Row starter offer (chest slot with -50% tag, name, 23h countdown pill, $1.99), and sm Tabs Gems / Coins / Items (Items with a Notification Dot that clears) switching 3-column Shop Card grids via `data-panel`. Gems cost real money, coins cost gems, and items cost coins. One `buy` listener handles store stubs, balance checks (error toast), counter updates and floats. Kit fix: `core.css` also makes `[role="tabpanel"][hidden]` always hide, so custom grid panels switch correctly.
- Tested: Opened at 375×812. Only the selected panel shows. Buying 1000 coins for 10 gems gives 85→75 gems and 2400→3400 coins. The Items tab clears its alert, and buying clover for 3000 coins works. Everything fits with no scroll.
- Notes for next agent: Three tabs with icons need `data-size="sm"` at 400px width. Remember to load `alert.css` when using `data-alert`, or the `!` image renders huge.

## v0.36.0-A — Settings block
- Agent: A (Claude) · Date: 2026-09-15
- Done: Added `kit/blocks/settings.html`, a SETTINGS popup opened from a settings icon button. First panel: Sound and Music Toggles (with icons), each with a full-width sm volume Slider showing a percent, and a Vibration Toggle. Second panel: language Tabs (EN/ES/DE/TR) and a Notifications Checkbox. Also Support (mail icon), Privacy and Restore purchases buttons, plus version text. One `change` listener saves every control via `data-setting`; `input` is ready for live volume.
- Tested: Opened at 375×812. The popup (679px) fits. Vibration toggle, language tab, notifications checkbox and music slider each fire change with the right key/value (vibration true, language de, notifications false, musicVolume 30).
- Notes for next agent: Sliders need their own full-width row inside a popup; next to a label + toggle they collapse to just the thumb.

## v0.35.0-A — Daily Reward block
- Agent: A (Claude) · Date: 2026-09-15
- Done: Added `kit/blocks/daily.html`: a menu calendar button with a Notification Dot opens a `DAILY REWARD` popup (DAY 3 sub-tag). The 7-day grid of Reward Slots is built from a data array: past days claimed, today white with a TODAY tag + alert, future days dimmed, and day 7 a wide chest slot. Claim floats the reward, counts coins up, re-renders today as claimed, starts a "19h 0m" next-reward pill timer and clears the menu alert. Kit fix: `core.css` now makes `[hidden]` always hide any `sc-*` element (component display styles used to override it), and the rule is added to AGENTS.md.
- Tested: Opened at 375×812. The popup fits, the timer is hidden before claiming, Claim adds 250 coins (1200 → 1450), day 3 becomes claimed, the timer shows and the alert clears. All 17 component test pages still pass with the core.css change.
- Notes for next agent: Blocks that render slots from data use `innerHTML`; the runtime upgrades the inserted slots automatically.

## v0.34.0-A — Reward Reveal block
- Agent: A (Claude) · Date: 2026-09-15
- Done: Added `kit/blocks/reward.html`, a chest-opening reveal on a solid Screen Shell. Closed step: EPIC CHEST banner (drop) and a shaking `chest` with a pulsing glow, plus "Tap the chest to open". Tapping swaps to the NEW SKIN! banner (unfurl, same spot), pops the `helmet` item in, shows the name + EPIC tag and a row of 3 Reward Slots (popIn), floats EPIC!, and reveals Collect.
- Tested: Opened at 375×812. Both steps fit with no scroll, the tap switches the step, the banner/item/rewards animate, and Collect hides the screen.
- Notes for next agent: The glow and shake are block-local layout glue (tiny keyframes). If more blocks need them, promote them to a kit component instead of copying.

## v0.33.0-A — Start block
- Agent: A (Claude) · Date: 2026-09-15
- Done: Added `kit/blocks/start.html`, the home/start screen. It has a Top Bar (avatar + level 12 + name, coins short format, gems with +), side flat icon-button shortcuts (Daily with Notification Dot, Mail with a red count bubble, Settings, Gift with a FREE tag), a gold title with the level name, and a big yellow PLAY. An always-visible Bottom Tab Bar layer switches Home / Shop / Rank screens via `data-panel` (the Shop alert clears when opened). PLAY hides the menu layers and shows a gameplay layer with a back-home button.
- Tested: Opened at 375×812. The title fits, and the side buttons, top bar and tab bar are inside the edges. Shop tab shows the shop screen and clears its alert, Home returns, PLAY hides menu + nav and shows the play layer, and back-home restores both.
- Notes for next agent: Keep game titles short (about 8 characters at the default Screen Title size) or the title touches the edges.

## v0.32.0-A — Pause block
- Agent: A (Claude) · Date: 2026-09-15
- Done: Added `kit/blocks/pause.html`, a pause menu over a frozen stand-in game. A HUD pause button opens the `PAUSED` popup (LEVEL 12 sub-tag, static backdrop). It has quick settings in a panel (Sound/Music/Vibration Toggles with the new `sound`/`music` icons, right-aligned) and stacked Resume (lg green) / Restart (restart icon) / Home (home icon). Toggles fire `change` for the game to apply and save.
- Tested: Opened at 375×812. Toggles line up at the same right edge, the Vibration toggle switches ON, and Resume closes the popup and unfreezes the game.
- Notes for next agent: Rows inside `.sc-panel` need `align-self:stretch; width:100%` or they shrink to content.

## v0.31.0-A — Fail block
- Agent: A (Claude) · Date: 2026-09-15
- Done: Added `kit/blocks/fail.html`, the level-failed screen over the game. It has a dim Screen Shell with a gem counter, `FAILED` red title (shake), empty arc stars, "So close!" with a 78% orange progress bar, and a timed continue offer: "Continue?" + ring timer (8 s, warn at 3). Revive by video or for 20 gems (toast if short), plus Retry (restart icon) and Give up buttons. The offer hides when the timer ends.
- Tested: Opened at 375×812. The layout fits with no scroll, the timer counts down and the offer hides at 0, and the gem check works.
- Notes for next agent: The continue offer uses `visibility:hidden` so the layout doesn't jump when it expires.

## v0.30.0-A — Success block
- Agent: A (Claude) · Date: 2026-09-15
- Done: Added `kit/blocks/success.html`, the level-complete screen over the game. It has a dim Screen Shell with a coin counter, `CLEAR!` title (drop), an animated arc Star Rating, an XP bar with Level Badge that fills after the stars, a REWARDS divider and 4 Reward Slots popping in (`SC.popIn`), and Claim / x2 Claim (video icon) buttons plus a Home icon button. Claim floats +coins, counts the counter up, marks slots claimed and disables the buttons.
- Tested: Opened at 375×812. The layout matches the old demo, with everything inside the edges and no scroll. x2 Claim adds 1000 coins (1250 → 2250), all slots show claimed, and the buttons disable.
- Notes for next agent: The rewards grid is 4 columns of md slots (fits 400px). Use 3 columns or `data-size="sm"` slots for more rewards.

## v0.29.0-A — Gameplay HUD block
- Agent: A (Claude) · Date: 2026-09-15
- Done: Started Blocks. Added `kit/blocks/hud.html`, a complete in-game HUD built only from kit components over a stand-in canvas. Top row: pause, a star-marker score bar and coins. Second row: lives counter and timer pill. Boosters with count bubbles at the bottom. It also has a Pause popup that pauses/resumes the timer and restarts. Taps score, count coins up, float +10, and pop STAR! at markers. Added `blocks/README.md`, a `blocks` list in `registry.json`, a "Blocks" group in the docs menu, and a "Done — blocks" table in STATUS. AGENTS.md file map now lists `blocks/` and `tools/tests/`.
- Tested: Opened at 375×812. Taps update score/coins with floats, the star marker fires, boosters decrement their badges, Pause opens the popup and pauses the timer (00:58 held), Resume closes it. Nothing scrolls and there are no console errors from the page.
- Notes for next agent: Blocks are pages, not components: no test page, but check each at 375×812. Toasts cover the top bar in HUDs; use `SC.float(..., null, {style:'pop'})` for mid-screen celebrations instead.

## v0.28.0-A — Tutorial Hand component
- Agent: A (Claude) · Date: 2026-09-15
- Done: Added `SC.tutorial.point(target, {gesture, to, text, spotlight, once})` → Promise and `SC.tutorial.clear()` / `SC.tutorial.active`. It shows the kit `hand` icon with its fingertip placed exactly on the target, a tap ripple, swipe (up/down/left/right) and drag-to-destination animations, and an optional Hint Bubble. The spotlight dims the screen with a rounded hole (box-shadow) and 4 transparent blockers, so only the target is tappable. It follows moving targets. Hint bubbles now render above the spotlight. Added the AI manual, registry item, docs page (live 3-step tutorial, gesture previews) and `tools/tests/tutorial.html`. This completes the component list.
- Tested: `tools/tests/index.html`: all 17 pages pass (adds tutorial 14/14, covering parts, fingertip position, spotlight blocking, target tappable, hint above dim, promise resolve/clear, no-spotlight drag vars, once:false, replacement, invalid target). Live docs tutorial walks through all 3 steps.
- Notes for next agent: The fingertip offset is `TIP = {x:.17, y:.05}` of the 76px hand box (measured from `hand.png`). If the hand image is replaced, re-measure it.

## v0.27.0-A — Shop Card component
- Agent: A (Claude) · Date: 2026-09-15
- Done: Added `.sc-shopcard`: a glossy shop offer card in 8 colors. It has a kit-icon pack picture with a radial glow and an "x500" amount, an optional bonus line, a corner tag (Shop Card is now a Tag host), and a green `.sc-button` price that is real-money text or in-game currency with `data-price-icon`. `data-state="sold"` greys it and disables "SOLD". The `buy` event carries `{price, currency}`. Added the AI manual, registry item, docs page (real/currency prices, colors, sold, live buy-with-coins with toast + float) and `tools/tests/shopcard.html`.
- Tested: `tools/tests/shopcard.html` 10/10 (parts, real vs currency buttons, aria, buy event detail, sold on/off, attribute updates, no duplicates/churn). Live docs demo spends coins and shows the not-enough toast.
- Notes for next agent: The price button is a normal `.sc-button` built by the runtime. Changing `data-price-icon` or `data-state` re-syncs its icon.

## v0.26.0-A — Top Bar component
- Agent: A (Claude) · Date: 2026-09-15
- Done: Added `.sc-topbar` for home screens. The player block is a button with a framed avatar kit icon, a Level Badge on its corner and the name, and fires `profile`. Resource Counters placed inside (even added later) move to the right group. The name shrinks and fades first so counters always fit. Long titles in Top Bar and Item Row now fade out (`.sc-long` via `markLong`) instead of an ellipsis, which broke the outlined text copy. Added the AI manual, registry item, docs page (home screen with tab bar, variants, live profile/earn) and `tools/tests/topbar.html`.
- Tested: `tools/tests/index.html`: all 15 pages pass (adds topbar 11/11, covering structure, avatar/level/name, button semantics, fit at 376px, long-name fade, profile event, attribute updates/removal, late counters, no duplicates/churn).
- Notes for next agent: Don't use `text-overflow: ellipsis` on `.sc-text`: its `::before` outline copy isn't truncated and leaves a black smudge. Use the `.sc-long` fade pattern. The Resource Counter's "+" button overhangs its box by ~2px.

## v0.25.0-A — Level Badge component
- Agent: A (Claude) · Date: 2026-09-15
- Done: Added `.sc-level`: the `level-badge` shield with an outlined number, 3 sizes, and `aria-label` "Level N". `SC.setValue(level, n)` pops on change. Progress Bar now accepts `data-level` to put the badge on its left end (XP bar, min 30px on thin bars). Added the AI manual, registry item, docs page (sizes, XP bars, live gain-XP level-up) and `tools/tests/level.html`.
- Tested: `tools/tests/level.html` 13/13 (image/number/aria, size and centering, badge on bar + overlap + minimum size, setValue pop only on change, data-level change/removal, progress setValue keeps badge, inserted badge, no duplicates/churn). Visual check of docs.
- Notes for next agent: `upgradeProgress` now builds `.sc-level` from `data-level`. Don't combine it with the progress `data-icon`.

## v0.24.0-A — Notification Dot component
- Agent: A (Claude) · Date: 2026-09-15
- Done: Added the Notification Dot, a "something new" marker. `data-alert` on buttons, icon buttons, slots, tabs and tab bar items shows the red `alert` icon (bare) or a small plain dot (`dot`) on the top-right corner, with pop-in + gentle pulse; on tab bar items it sits on the icon corner. Standalone `.sc-alert` works inline. `SC.setAlert(el, true|false|'dot')`. Coexists with tags and badges. Added the AI manual, registry item, docs page (hosts, tab bar, live clear-on-open) and `tools/tests/alert.html`.
- Tested: `tools/tests/index.html`: 13 pages pass (adds alert 13/13, covering icon vs dot, coexistence with tag/badge, tabs, position, standalone, setAlert switching/removal, attribute changes, no duplicates/churn).
- Notes for next agent: Not supported on `.sc-row-avatar` (it has overflow:hidden). Geometry checks must wait ~450ms for the pop-in scale animation.

## v0.23.0-A — Loading Bar component
- Agent: A (Claude) · Date: 2026-09-15
- Done: Added `.sc-loading` for the start/loading screen: a large glossy progress bar with "Loading… 42%", an optional bouncing kit icon and rotating tips (`data-tips="a|b"`, every 3 s). It has `data-color`/`data-label`, progressbar semantics, and `SC.loading.set(el, pct)` (clamped; fires `done` once at 100). `SC.loading.done(el)` fills it and hides its Screen Shell. Added the AI manual, registry item, docs page (hero + live simulated load that switches to a play screen) and `tools/tests/loading.html`. STATUS image notes now point to the new icons.
- Tested: `tools/tests/loading.html` 12/12 (parts built once, label, bar value/color, aria, tips rotate, clamp both ways, done once, attribute re-render, done() hides shell). Live docs demo loads and reveals PLAYING!. All other test pages still pass.
- Notes for next agent: `upgradeLoading` owns a tip interval per element (`el._scTips`); it stops when the element leaves the page.

## v0.22.0-A — Item Row component
- Agent: A (Claude) · Date: 2026-09-15
- Done: Added `.sc-row`, a colored card row layout matching the reference mission and leaderboard rows. It has 8 colors (plain dark titles on white/yellow, outlined white on the others), a `leader` variant (rank badge + framed avatar + title + trophy score), a `done` state, and row parts `.sc-row-body/-title/-rank/-avatar/-score` that auto-build kit text and icons. Kit parts inside (slot, progress, button) work as usual. Also relabelled the Tab Bar's home item as Home. Added the AI manual, registry item, docs page (missions, leaderboard, friend row, live claim) and `tools/tests/row.html`.
- Tested: `tools/tests/index.html`: 11 pages pass (adds row 11/11, covering text/icons, plain vs outlined titles, long title doesn't widen the row, nested parts, leader size, score alignment, setLabel/icon swap, inserted rows, no churn). Visual comparison with the reference sheet.
- Notes for next agent: `.sc-row-title/-rank/-score` are in TEXT_COMPONENTS and `.sc-row-avatar/-score[data-icon]` in ICON_COMPONENTS, so they use the generic text/icon upgrade path. The row needs `min-width:0` or long titles stretch it inside grid/flex parents.

## v0.21.1-A — 16 new icons (icons4 sheet)
- Agent: A (Claude) · Date: 2026-09-15
- Done: Cropped the owner's `icons/icons4.png` into `kit/assets`: home, shop, helmet, play, sound, sound-off, music, music-off, menu, restart, alert, level-badge, hand, avatar, gem-pile, coin-pile. Regenerated `offsets.css`, added the names to `registry.json → icons`, and switched the Tab Bar docs to the real home/shop icons. The prompt is saved in `icons/PROMPT-icons4.md`.
- Tested: Visual contact sheet of all 16 crops (each one clean, single icon). All test pages still pass.
- Notes for next agent: Top Bar, Level Badge (`level-badge`), Notification Dot (`alert`), Shop Card (`gem-pile`, `coin-pile`) and Tutorial Hand (`hand`) are no longer blocked. Use sound/music icons in settings examples.

## v0.21.0-A — Toast Message component
- Agent: A (Claude) · Date: 2026-09-15
- Done: Added `SC.toast(text, {kind, icon, duration, pos})`: a glossy pill message (info dark / success green / error red / reward gold) with outlined kit text and an optional kit icon. It slides in at the top or bottom (12px + safe area) and removes itself. Separate queues for top and bottom show one at a time, with at most 3 waiting and repeated text dropped. It never blocks taps and uses an aria-live polite layer. Added the AI manual, registry item, docs page and `tools/tests/toast.html`.
- Tested: `tools/tests/index.html`: 10 pages pass (adds toast 12/12, covering show, kind/icon, live region, 12px layer offset, queue order, duplicate drop, cap, parallel bottom queue, drain). Live docs demo queues error → reward with a separate bottom toast.
- Notes for next agent: Measure the fixed `.sc-toast-layer`, not the toast, in tests: the toast is mid slide-in animation.

## v0.20.0-A — Hint Bubble component
- Agent: A (Claude) · Date: 2026-09-15
- Done: Added the Hint Bubble: a white speech bubble with an outlined border and a rounded rotated-square pointer (no polygons) in 4 directions, 2 sizes. `data-hint` on any element shows it on tap (auto-hides after 2.5 s, on a second tap or a tap elsewhere). `SC.hint.show(target, text, {pos, duration})` / `SC.hint.hide(target?)` handle tutorials (`duration: 0` stays). Floating bubbles are placed next to the target, clamped 12px inside the screen with the pointer still aiming at the target, scale with the target's Screen Shell, reposition on resize/scroll, and never block taps. Added the AI manual, registry item, docs page, `tools/tests/hint.html` and `icons/PROMPT-icons4.md` (owed image prompt).
- Tested: `tools/tests/index.html`: 9 pages pass (adds hint 15/15, covering static pointer, tap show/hide, positions, pointer aim, edge clamp, code hints vs outside taps, replace, duration, hide all). Visual check of all pointer directions and tap demos.
- Notes for next agent: Bubble geometry tests must wait ~300ms for the pop-in `scale` animation before measuring rects.

## v0.19.0-A — Title Banner Ribbon component
- Agent: A (Claude) · Date: 2026-09-15
- Done: Added `.sc-banner`, a ribbon banner with a glossy band (outlined kit text) and darker folded tails behind both ends, built from skewed rounded pseudo-elements (no polygons). It has 10 colors, 3 sizes and `unfurl`/`drop` entrance animations. The runtime wraps the text in `.sc-banner-band` so the tails render behind the band. Works with `SC.setLabel` and `SC.replay`. Added the AI manual, registry item, docs page and `tools/tests/banner.html`.
- Tested: `tools/tests/index.html`: 8 pages pass (adds banner 9/9). Visual check of hero, sizes, colors and the live rename/replay demo.
- Notes for next agent: Tails use z-index:-1 inside an isolated `.sc-banner`, so the band must be its own element (z-index 1). Otherwise the tails paint over the band background.

## v0.18.0-A — Tag Ribbon component
- Agent: A (Claude) · Date: 2026-09-15
- Done: Added `.sc-tag`, small glossy sticker labels (NEW, HOT, BEST, SALE, -50%, x2) in all 10 kit colors, 3 sizes, with optional tilt. Buttons, icon buttons and tabs accept `data-tag` + `data-tag-color` + `data-tag-pos` (top-left/top-right tilted, or top centered). The runtime builds and updates the sticker, and it pops in. Reward Slot keeps its own tag. Added the AI manual, registry item, docs page and `tools/tests/tag.html`.
- Tested: `tools/tests/index.html`: 7 pages pass (bubble 60, toggle 39, slider 30, checkbox 20, tabs 24, tabbar 13, tag 15). Visual check of all docs examples.
- Notes for next agent: `data-tag*` attribute changes on slots still go to `upgradeSlot` (the tag branch only handles TAG_HOSTS). Standalone tags are matched as `.sc-tag:not(.sc-tag-attached)`.

## v0.17.0-A — Bottom Tab Bar component
- Agent: A (Claude) · Date: 2026-09-15
- Done: Added `.sc-tabbar`, the bottom navigation bar for home screens, matching the reference. It's a dark navy bar. The selected item rises on a glossy indigo block with rounded free top corners and sharp attached bottom corners, a bigger icon and an uppercase label. It has count badges on icons, 9 block colors, disabled items and `data-panel` to switch screens. Inside `.sc-screen-bottom` it bleeds to the phone edges and pads the home-bar safe area. It shares the Tabs runtime (`SC.tabbar === SC.tabs`). Also added `tools/tests/index.html`, which runs every component test page at once (AGENTS.md §4 updated). `setSpan` and the bubble title now only write when the value changes.
- Tested: `tools/tests/index.html`: all 6 pages pass (bubble 60, toggle 39, slider 30, checkbox 20, tabs 24, tabbar 13). Tab bar checks cover item class, selection, labels only on selected, badges, panels, edge bleed inside a scaled shell, click/disabled/keys and no attribute churn. Live docs demo switches 4 screens and clears the Chests badge.
- Notes for next agent: The tab bar has no home/shop icons yet (uses cash/chest/star/trophy/settings). Swap in real ones after `icons4.png` arrives. Tabs and tab bar share `upgradeTabs`; the item class depends on the parent (`sc-tab` vs `sc-tabbar-item`).

## v0.16.0-A — Tabs component
- Agent: A (Claude) · Date: 2026-09-15
- Done: Added `.sc-tabs`, a segmented row of 2–4 tabs matching the reference: glossy blue selected tab and muted dark purple unselected tabs with a thin light top edge. Supports optional kit icons, 9 selected colors, 3 sizes, `data-badge` on tabs (Count Bubble now accepts `.sc-tab` hosts), disabled tabs, and `data-panel` to auto show/hide content. It has full tab semantics (tablist/tab, aria-selected, roving tabindex, aria-controls), Left/Right/Home/End keys, a `change` event and `SC.tabs.get/set`. Added the AI manual, registry item, docs page and `tools/tests/tabs.html`.
- Tested: `tools/tests/tabs.html` 24/24 passed, covering initial/fallback selection, roles, icons, panels, click/disabled/no form submit, keyboard wrap, silent set/emit, attribute change, badges, appended tabs, repeated upgrades, equal widths and no observer loop. Visual check in the docs against the reference sheet. Checkbox 20/20, Slider 30/30, Toggle 39/39 and Bubble 60/60 still pass.
- Notes for next agent: `sc.js` has a shared `setAttr(el, k, v)` helper that only writes real changes; use it in new builders to avoid MutationObserver loops. In tests, use `:scope >` when counting `.sc-text`, because a badge bubble contains its own `.sc-text`.

## v0.15.0-A — Checkbox component
- Agent: A (Claude) · Date: 2026-09-15
- Done: Added `.sc-checkbox`, a chunky tick box. Unchecked is a dark inset box. Checked is a glossy colored box with the kit `check` icon, which pops in. It has an optional outlined text label, 10 colors, 3 sizes and native disabled. Uses `role=checkbox` + `aria-checked` and one `change` event per tap/Space/Enter. API: `SC.checkbox.get/set/toggle` (silent unless `{emit:true}`, boolean-only like Toggle). Added the AI manual, registry item, docs page and `tools/tests/checkbox.html`.
- Tested: `tools/tests/checkbox.html` 20/20 passed, covering states, click, disabled, no form submit, silent set/emit/throw, attribute re-sync, setLabel, dynamic insert and no observer loop. Real clicks checked in the docs. Slider 30/30, Toggle 39/39 and Bubble 60/60 still pass.
- Notes for next agent: Never reuse a CSS variable name inside its own definition (`--fs:var(--fs)` breaks the label size). Checkbox uses `--cb-fs`. Checkbox patterns mirror Toggle.

## v0.14.0-A — Slider component
- Agent: A (Claude) · Date: 2026-09-15
- Done: Added `.sc-slider`, a glossy track with a round white thumb (same thumb style as Toggle). It supports drag, tap-to-jump, arrows, Page Up/Down, Home and End. Options: `data-min/max/step` (decimals ok), `data-label` percent/value, 9 fill colors, 3 sizes (touch area ≥ 44px), an optional left icon, and `disabled` (also inside a disabled fieldset). Events: `input` while moving and `change` on release. API: `SC.slider.get/set` (silent unless `{emit:true}`, invalid values ignored). Added the AI manual, registry item, docs page and `tools/tests/slider.html`.
- Tested: `tools/tests/slider.html` 30/30 passed, covering keyboard, pointer drag/clamp/release, API, attribute re-render, labels, disabled, dynamic insert, pointer math inside a scaled `.sc-screen`, and no observer loop. Real mouse drag and keys checked in the docs. Phone size 375×812 has no horizontal overflow. Codex's Toggle 39/39 and Bubble 60/60 still pass.
- Notes for next agent: `sc.js` now observes `disabled`, `data-min` and `data-step`. Inside `upgradeSlider`, only set attributes when they really change, or the MutationObserver loops. Sound/music icons are still missing (owed image prompt).

## v0.13.0-B — Toggle component
- Agent: B (Codex / GPT) · Date: 2026-09-15
- Done: Added a glossy ON/OFF settings switch with a sliding circular thumb, three sizes, kit ON colors, disabled states, keyboard focus and reduced-motion support. Bare `data-checked` or `data-checked="true"` turns it ON; missing/false turns it OFF. Added `SC.setChecked`, `SC.toggle.get/set/toggle`, and one bubbling `change` event per user activation. Includes the AI manual, registry and live docs.
- Tested: Docs in a browser at 375×812 and 1280×900, with no horizontal overflow. Checked state, sizes, colors, disabled examples, code tabs, keyboard focus, tap/Space/Enter, silent restore, lock/unlock and dynamically added options. All 39 Toggle regression checks and all 60 Count Bubble checks passed. Existing Screen Shell demo still starts, pauses and resumes. JavaScript syntax, registry paths/version consistency and `git diff --check` passed; no browser warnings/errors in the checked pages.
- Notes for next agent: Screen Shell was completed by Claude while Toggle was being built; Toggle was developed separately, then integrated after v0.12.0-A. Use a native button and a stable accessible name. Runtime owns `aria-checked`; the game owns saving and side effects. Helpers are silent unless `{ emit: true }` is passed, and `SC.setChecked` requires a boolean. Native disabled fieldsets now suppress press feedback too. Regression page: `/tools/tests/toggle.html`. Next: Slider.

## v0.12.0-A — Screen Shell component
- Agent: A (Claude) · Date: 2026-09-15
- Done: Added `.sc-screen`, the full-page layout every game screen starts from. It has top / middle / bottom regions and scales a 400×870 design to any phone shape. It never scrolls, keeps 12 real px + safe-area margins, and offers `data-backdrop` none/dim/solid (none lets taps reach the game), `data-enter` fade/pop, `data-fit="parent"` for previews, and `SC.screen.show/hide/fit` with `show`/`hide` events. Added the AI manual, registry item, docs page and a full example `examples/screen-on-canvas.html` (start → HUD → pause over a tappable canvas).
- Tested: Browser, docs at desktop width and the example at 375×812. Edge gaps measured exactly 12px on top/left/right/bottom. No page scroll. A tap on empty HUD space hits the canvas. Tall/wide/short frames all keep bars at the edges. Pause/resume switching works. Title/stars entrance animations replay when a hidden screen is shown. Codex's `tools/tests/bubble.html` still passes 60/60 after the `sc.js` change.
- Notes for next agent: the shell uses `transform: scale()`, so a `position:fixed` child is positioned relative to the shell. Keep popups outside screens. Bottom region has `margin-top:auto`, so it stays at the bottom even without a middle.

## v0.11.0-B — Count Bubble component
- Agent: B (Codex / GPT) · Date: 2026-09-15
- Done: Added glossy corner counts to Button, Icon Button and Reward Slot through `data-badge`, optional `data-badge-color`, and `SC.setBadge()`. Counts update automatically, including on newly inserted components. Zero stays visible; counts above 99 display as 99+; missing or invalid counts hide. Added the AI manual, registry entries and live docs. Kept icon buttons round and label updates separate from badge text.
- Tested: Browser preview at 375×812 and normal desktop width; all examples, palette colors, images, live use/refill/hide/add controls, and code tabs. 60 browser regression checks passed in `tools/tests/bubble.html`, covering all hosts, attribute and API updates, invalid values, removal, repeated upgrades, label/icon preservation, round sizes/variants, and press feedback. JavaScript syntax, registry links/version consistency and `git diff --check` passed.
- Notes for next agent: Count Bubble sits top-right to avoid the slot quantity at bottom-right. Load bubble CSS plus the selected host CSS. Leave 8px outside the host and keep the whole badge inside screen margins. Avoid overlapping long slot tags. Accessible labels remain game-owned. Preview regression checks at `/tools/tests/bubble.html`. Next: Screen Shell.

## v0.10.2-A — Repo made private
- Agent: A (Claude) · Date: 2026-09-15
- Done: GitHub repo switched to private at the owner's request. GitHub Pages (live docs site) is therefore offline. Removed live-site links from README, AGENTS.md, STATUS.md.
- Tested: `gh repo view` reports PRIVATE.
- Notes for next agent: preview only locally with `tools/serve.py`.

## v0.10.1-A — Clean up project folder
- Agent: A (Claude) · Date: 2026-09-15
- Done: Moved early experiments (home screen, blueprint button, fonts tests, loose images) and all reference screenshots into `_archive/` (local only, gitignored). Moved old pre-kit demo pages into `super-casual/old-demos/`. Rewrote README, updated links in `index.html`, AGENTS.md and STATUS.md.
- Tested: local server: index, kit docs, kit icons, old demo pages and their images all return 200.
- Notes for next agent: `_archive/` exists only on the owner's Mac. Never commit it. Old demos are at `super-casual/old-demos/`.

## v0.10.0-A — Super Casual kit: 10 components + multi-agent handoff system
- Agent: A (Claude) · Date: 2026-09-15
- Done:
  - Built the shadcn-style kit in `super-casual/kit`: `core.css`, `sc.js` runtime, `registry.json`, per-component CSS + AI manual + docs page.
  - Components: Button, Icon Button, Resource Counter, Reward Slot, Popup, Progress Bar, Screen Title, Star Rating, Countdown Timer, Floating Text.
  - 31 icons in `kit/assets` with automatic optical centering (`tools/icon_offsets.py`).
  - Old demo screens (`super-casual/success.html`, `fail.html`, `pause.html`, `hud.html`) kept as reference for future Blocks.
  - Added `AGENTS.md`, `CLAUDE.md`, `STATUS.md`, `CHANGELOG.md` so Claude and Codex can take turns.
- Tested: every docs page was checked in a browser. Examples render, icons load, and live demos work (star earn/lose pops one by one, timer start/pause/+5s/done, counter count-up, popup open/close).
- Notes for next agent:
  - Star Rating: when stars turn off, the pop animation class must be cleared, or they stay visually filled.
  - Popup docs show inline copies with class `.inline`; real popups are full-screen.
  - Use `tools/serve.py` for previews (no caching).
