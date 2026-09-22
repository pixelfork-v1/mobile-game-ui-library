# Action Buttons

Round glossy buttons for game actions (jump, fire, dash). They pair with the Joystick on the opposite side of the screen and report `press` and `release`, so holding works.

## Install

```html
<link rel="stylesheet" href="kit/core.css">
<link rel="stylesheet" href="kit/components/actions/actions.css">
<link rel="stylesheet" href="kit/components/bubble/bubble.css">   <!-- only for data-badge counts -->
<script src="kit/sc.js"></script>
```

## Usage

```html
<div class="sc-actions" id="acts" data-layout="cluster">
  <button class="sc-action" data-value="dash" data-icon="rocket" data-color="yellow" data-size="sm">Dash</button>
  <button class="sc-action" data-value="jump" data-icon="jump" data-color="green" data-size="lg">Jump</button>
</div>

<script>
  acts.addEventListener('press',   e => game.start(e.detail.value));
  acts.addEventListener('release', e => game.stop(e.detail.value));
</script>
```

## Options

| Attribute | Values | Default | Notes |
|---|---|---|---|
| `.sc-actions` `data-layout` | `cluster` `row` `column` `grid` | `cluster` | Cluster staggers the buttons for a thumb. |
| `data-value` | text | required | Name the game receives. |
| `data-icon` | kit icon or path | | Picture. |
| `data-size` | `sm` `md` `lg` | `md` | 56 / 72 / 92 px. |
| `data-color` | kit colors | `sky` | |
| `data-badge` | number | | Count left (needs bubble.css). |
| text inside | text | | Small label under the icon. |
| `disabled` | boolean | | Locked / on cooldown. |

Events fire on the `.sc-actions` group (or on the button if it has no group): `press` and `release`, both with `detail.value`.

## Rules for AI agents

- 1–3 buttons on a phone. Main action `lg`, bottom-right; helpers smaller and higher.
- Always pair with the Joystick on the other side inside `.sc-screen-bottom`.
- Handle both `press` and `release` so tap and hold both work.
- `data-badge` for limited actions, `disabled` during cooldown.


> Style: **Cozy Paper**. Same markup, attributes and events as every other style of this kit —
> only the CSS differs. See ../../STYLE.md.
