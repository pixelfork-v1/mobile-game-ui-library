# Speedometer

Shows how fast the player is going in car, bike, boat and other vehicle games. Two types: a round **dial** with a needle, a green fill and a red zone, or a half **arc** that fills from green to yellow to red. The number and the unit are in the kit's outlined text.

## Install

```html
<link rel="stylesheet" href="kit/core.css">
<link rel="stylesheet" href="kit/components/speedometer/speedometer.css">
<script src="kit/sc.js"></script>
```

## Usage

```html
<div class="sc-speedometer" id="speedo" data-value="0"></div>                  <!-- dial -->
<div class="sc-speedometer" id="speedo" data-type="arc" data-value="0"></div>  <!-- arc -->

<script>
  function frame() {
    SC.setValue(speedo, car.speed * 3.6);   // every frame; m/s → km/h
    requestAnimationFrame(frame);
  }
</script>
```

The gauge builds itself from its attributes. `SC.setValue()` never animates: the needle and the number follow the value exactly, so call it every frame.

## Options

| Attribute      | Values | Default | Notes |
|----------------|--------|---------|-------|
| `data-type`    | `dial` `arc` | `dial` | Dial: disc, 240° scale from lower left (0) to lower right (max), needle. Arc: 180° bar over the top |
| `data-value`   | number | `0` | Current speed, in the game's units. Below 0 shows 0. Above the max the needle / arc stop at the max, the number shows the real value |
| `data-max`     | number | `140` | Top of the scale |
| `data-unit`    | text | `km/h` | Small text under the number. `""` hides it |
| `data-redline` | number | 80% of max | Dial only: where the red zone starts. The green fill stops there |
| `data-size`    | `sm` `md` `lg` | `md` | Dial 96 / 120 / 150 px wide · arc 120 / 150 / 190 px wide |

The number shown is the value rounded to a whole number.

## Examples

```html
<!-- Car HUD: dial in the lower-left corner, above the Brake button -->
<div class="sc-screen" id="hud">
  <div class="sc-screen-bottom">
    <div style="display:flex; justify-content:space-between; align-items:flex-end; width:100%">
      <div style="display:flex; flex-direction:column; align-items:center; gap:8px">
        <div class="sc-speedometer" id="speedo" data-value="0"></div>
        <button class="sc-button" data-color="red" data-size="sm" id="brake">Brake</button>
      </div>
      <button class="sc-button" data-color="green" data-size="sm" id="gas">Gas</button>
    </div>
  </div>
</div>

<!-- Arc centred between the pedals -->
<div style="display:flex; justify-content:space-between; align-items:flex-end; width:100%">
  <button class="sc-button" data-color="red" data-size="sm">Brake</button>
  <div class="sc-speedometer" data-type="arc" data-size="sm" data-value="0"></div>
  <button class="sc-button" data-color="green" data-size="sm">Gas</button>
</div>

<!-- Miles per hour, a faster car, an earlier red zone -->
<div class="sc-speedometer" data-max="180" data-unit="mph" data-redline="140"></div>

<!-- No unit -->
<div class="sc-speedometer" data-type="arc" data-unit=""></div>
```

## JavaScript

```js
SC.setValue(speedo, speed);                                      // every frame: no animation, no bump
SC.setValue(speedo, body.getLinearVelocity().length() * 3.6);    // physics in m/s → km/h
speedo.dataset.max = '200';                                      // attributes can change at any time
```

It only moves the needle / arc and changes the number (the parts are built once), so 60 calls a second are cheap.
Accessibility: `role="meter"` with `aria-valuenow`, `aria-valuemin`, `aria-valuemax`, `aria-valuetext` ("72 km/h") and `aria-label="Speed"` unless you set your own.

## Rules for AI agents

- **Car, bike, boat and other vehicle games show their speed with this.** One per screen.
- **Call `SC.setValue(el, speed)` every frame** from the game loop, with the speed in the game's units. Don't animate it yourself.
- **Units:** km/h by default. A 2D or 3D physics engine gives m/s: multiply by **3.6** for km/h (or by 2.237 and set `data-unit="mph"`). Use the speed's length, never a signed x velocity, so reversing doesn't show 0.
- **`data-max`** a little above the vehicle's real top speed, so the needle reaches the red zone only when it is really fast.
- **Placement:** the dial in a lower corner, above the Brake button; the arc centred at the bottom, between Brake and Gas. Inside the HUD's `.sc-screen-bottom`. Never over the middle of the road.
- **Display only:** taps go through it to the game. Never write its inner parts (svg, number, unit); show / hide it with the `hidden` attribute.
