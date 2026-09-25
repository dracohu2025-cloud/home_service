# GSAP + SVG pitfalls (learned the hard way)

Two classes of bugs shipped in the English pipe-burst video and were caught by user feedback + dense 0.5s screenshots. Treat this as a hard gate before any re-render.

## Bug A — Origin asymmetry (clock hands)

**Symptom**: Hands look correct during live scrub but land wrong in the final encode / seeked snapshot.

**Cause**: `tl.fromTo(el, { svgOrigin: "A" }, { svgOrigin: "B", rotation: … })` — from and to disagree on pivot. GSAP seeks by interpolating; inconsistent origins jump the pivot.

**Rule**: If you set `svgOrigin` or `transformOrigin`, set the **same** string in both from-vars and to-vars. Better for clocks: don’t use GSAP rotation at all — use SVG:

```html
<line id="minuteHand" transform="rotate(0 100 100)" ... />
```

```js
gsap.to("#minuteHand", {
  attr: { transform: "rotate(90 100 100)" },
  // or setAttribute in onUpdate
});
```

Native `rotate(angle cx cy)` keeps the pivot in the SVG coordinate system.

## Bug B — Transform attribute clobber (drip / drops)

**Symptom**: Element appears in the wrong place, flattened, or “abstract blue scribble” instead of the intended icon.

**Cause**: Element has `transform="translate(...) rotate(...)"` in the SVG markup, and GSAP also tweens `x` / `y` / `scale` / `rotation` on that same node. GSAP writes its own `transform` style/attribute and **overwrites** the authored one.

**Rule**:

1. Never GSAP-tween `x|y|scale|rotation` on a node that already has a `transform="..."` attribute.
2. Wrap the drawable in a clean `<g id="dropMotion">` with **no** transform attribute; put static transforms on an inner `<g>` or path; tween only `#dropMotion`.

```html
<g id="dropMotion"><!-- GSAP animates this -->
  <g transform="translate(40 20)"><!-- static layout stays here -->
    <path d="..." />
  </g>
</g>
```

## Bug C — Rotate without origin on pasted SVG groups

Pasted illustration groups often sit far from (0,0). GSAP `rotation` without `svgOrigin` rotates around the default origin and flies off-canvas.

**Rule**: Any rotation tween on an SVG group needs an explicit `svgOrigin` (and matching from/to — see Bug A).

## Automated gate

```bash
cd videos/burst-pipe-first-5-minutes
python3 scripts/qa-scan.py
# expect: zero issues
```

Flags:

| Code | Meaning |
|---|---|
| A | from/to origin mismatch |
| B | GSAP transform props on node that has `transform=` |
| C | rotation without svgOrigin on a transform-bearing group |

Do not merge/render if the scan reports issues.
