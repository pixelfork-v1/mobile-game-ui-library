# Joystick / D-Pad

On-screen movement control: a thumbstick or a 4-way D-pad, in the kit's glossy style. Works with touch, mouse and WASD / arrow keys.

## Install

```html
<link rel="stylesheet" href="kit/core.css">
<link rel="stylesheet" href="kit/components/joystick/joystick.css">
<script src="kit/sc.js"></script>
```

## Usage

```html
<div class="sc-joystick" id="stick" data-color="sky"></div>

<script>
  stick.addEventListener('move', e => player.move(e.detail.x, e.detail.y));  // -1…1, y+ is down
  stick.addEventListener('end', () => player.stop());
</script>
```

Follow-the-thumb version (the stick appears where the player touches):

```html
<div class="sc-joystick-zone" style="position:relative; flex:1; height:100%">
  <div class="sc-joystick" data-mode="follow"></div>
</div>
```

## Options

| Attribute | Values | Default | Notes |
|---|---|---|---|
| `data-variant` | `stick` `dpad` | `stick` | Thumbstick or 4-way pad. |
| `data-mode` | `fixed` `follow` | `fixed` | `follow` needs a `.sc-joystick-zone` parent. |
| `data-snap` | `free` `8` `4` | `free` | Directions reported to the game. |
| `data-size` | `sm` `md` `lg` | `md` | 120 / 150 / 180 px. |
| `data-color` | kit colors | `sky` | Knob / pad color. |
| `data-keys` | `false` | | Turns off WASD + arrow keys. |
| `data-arrows` | `false` | | Hides the direction arrows (clean stick or clean pad). |
| `data-knob` | `solid` `ghost` | `solid` | `ghost`: grey, half see-through middle, so it covers less of the game. |

The D-pad is drawn as **one continuous plus**, not four separate buttons: a dark plus for the outline and a
coloured plus on top of it, with an arrow at the end of each arm. Pressing a direction sinks that arm slightly.

## Events and JS

```js
stick.addEventListener('move', e => {
  // e.detail = { x, y, angle, distance, dir }
  // x,y: -1…1 · angle: degrees · distance: 0…1 (how far it's pushed) · dir: 'up' | 'up-right' | …
});
stick.addEventListener('end', () => {});   // released, x/y back to 0
SC.joystick.get('stick');                  // { x, y, angle, distance, dir, active }
```

## Rules for AI agents

- One joystick per game, bottom-left in `.sc-screen-bottom` of the HUD screen, with Action Buttons bottom-right.
- `free` for smooth movement, `8` for eight-way, `4`/`dpad` for classic movement.
- Use `follow` mode for full-screen games, `fixed` when the control must stay put.
- Use `distance` for speed and always handle `end` to stop the player.
- Never rebuild the inner parts; the runtime creates the knob, arrows and pad.
