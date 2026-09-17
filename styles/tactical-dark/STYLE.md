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
2. **"No sharp edges."** The reference leans on 45° cut corners and hexagons. Our rule also bans `clip-path`
   polygons. Recommendation: keep small radii (4–8px) and skip the cut corners — the look survives, because
   what carries it is the lit edge, not the corner. If you want the cut corners, that rule is relaxed for this
   style only, and the current kit keeps its rounded corners.

## Art

Icons do not carry over — the current 55 are chunky and glossy. This style needs flat, mostly single-colour
glyphs (white or accent), generated as their own sheets. Prompts live in `assets/IMAGE-PROMPTS.md` per style.
