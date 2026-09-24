## Video direction

**Register.** Premium consulting-grade explainer (Blue Professional, `frame.md`) with an upbeat, lively pulse: warm cream ground, one cobalt accent, near-black Space Grotesk headlines, soft cobalt-tinted cards with NO shadows, pill chrome. It must read expensive and calm-confident, never cartoonish — think a Stripe / Apple support explainer, not a sticker sheet. Energy comes from snappy timing, crisp kinetic type, and water in motion — not from bounce or clutter.

**Canvas.** 1920×1080. Every frame ground sets `container-type: size`; size in `cqw`/`cqh`. Full-bleed ground is its own `class="clip"` layer (never on `#root`). Captions are ON: a karaoke caption track owns the bottom ~17% — keep every element above y = 896px.

**Illustration kit (shared — never redraw).** Cobalt line-art SVGs live in `public/illustrations/`. Read the file and paste the `<svg>` markup INLINE (keep `viewBox`, size via CSS, prefix any ids you animate with the frame id to keep them unique). Animate the named inner groups:
- `house-cutaway.svg` (800×640): groups `#pipes` (paths `#pipe-main`, `#pipe-riser`, `#pipe-upper`, `#pipe-kitchen`, `#pipe-heater`), `#valve-main` (+ `#valve-main-wheel`, rotate about 196,522), `#meter`, `#burst-point`, `#spray`, `#puddle`, `#fixtures` (`#fx-tub`, `#fx-sink`, `#fx-heater`), `#breaker-panel`, `#room-labels`.
- `valve-gate.svg` (`#wheel`, rotate about 120,70 — clockwise = closing) · `valve-ball.svg` (`#lever`, rotate about 120,95; 0° = along the pipe = OPEN, 90° = across the pipe = CLOSED).
- `breaker-panel.svg` (`#switch-target`, `#switch-toggle` — slide the toggle right ~16 units = OFF) · `faucet.svg` (`#handle-hot`, `#handle-cold`, `#stream`) · `toilet.svg` · `water-heater.svg` (`#dial-needle`, `#flame`) · `phone-camera.svg` (`#viewfinder`) · `wrench.svg` · `shield-check.svg` (`#check`) · `tape-no.svg` · `valve-tag.svg` · `clock.svg` (`#hand-hour`, `#hand-minute`).
**Water in motion** is the signature: pipes carry flowing water as an animated cobalt dash (`stroke-dasharray` + `stroke-dashoffset` tweened linearly across the frame — a finite tween, never `repeat:-1`); when water is shut off the flow decelerates to a stop.

**Palette.** From `frame.md`: cream `#fdfae7` ground, cobalt `#1e2bfa` for every accent, near-black `#111111` headlines, muted `#6b6b6b` body, tinted cards (cobalt 4% fill, 20% 1.5px border, 12–14px radius, no shadow). **Semantic exception (small marks only, never fills or headlines):** red `#dc2626` = danger (the burst, electricity, "never"), green `#059669` = done (check marks). No other hues.

**Type.** Space Grotesk (headlines 600–700 near-black −0.02em; eyebrows uppercase 0.08em cobalt; every numeral cobalt 700 with `tabular-nums`) + Inter (body 400/500 muted). Load both from Google Fonts with a `<link>` inside the template: `https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;600;700&family=Inter:wght@400;500;600&display=swap`. On-screen copy is SHORT (labels, chips, one headline) — the captions carry the spoken sentence; never print the narration line.

**Shared chrome (every frame).** (1) Top-left eyebrow at (5cqw, 4.4cqh): a 60×4 cobalt accent-line, then `PIPE BURST PLAYBOOK` in the eyebrow style. (2) Top-right tag-pill at (right 5cqw, 4cqh) carrying the frame's section tag (given per frame). (3) A 3px cobalt progress bar pinned to the very bottom edge (y = 1077), its width = (frame number ÷ 9) × 100% — it grows from the previous frame's width to this frame's width over the first 0.6s. These three sit identically in all nine frames.

**Step layout (frames 4–8).** Left column (x 5cqw → 44cqw): a 56px-equivalent cobalt step-circle with the step numeral, the eyebrow `STEP 0N / 05`, the Space Grotesk `h2` step title, then 2–4 short chips / rows that reveal on their spoken cue. Right stage (x 50cqw → 95cqw, y 16cqh → 80cqh): one large tinted card holding the hero illustration that performs the action. Same positions in all five step frames — the consistent stage.

**Motion grammar.** One paused GSAP timeline per frame; every entrance `fromTo`; eases `power3.out` / `expo.out` for fast arrivals, `power2.inOut` for mechanical turns (valve wheel, lever, toggle). Snappy: most entrances 0.35–0.55s, text rises 2–3cqh with opacity, cards scale 0.96 → 1. Each reveal lands on the exact word time listed in its Scene line (word times are frame-relative seconds from the real voiceover). No bounce/elastic, no breathing loops, no slow back-half pans. Aliveness during holds = the water dash flow or live SVG internals only.

**Rhythm.** Frame 1 punchy cold open; frame 2 data beat; frame 3 a fast 3.5s "menu" snap; frames 4–8 the five-step run on one stage (push-slide LEFT between them); frame 9 closing CTA with the concentric-ring atmosphere and a clean end hold (the only real exit: fade the whole frame over the last 0.5s).

**Negative list.** No shadows on cards, no gradients, no glow/bokeh, no emoji, no cartoon faces, no stock-photo look, no square corners, no second accent color, no invented numbers, no narration sentences printed on screen, no slideshow (front-load then freeze), no screensaver (everything floating).

**Audio.** VO: MiniMax TTS (`audio_meta.json`, word-timed). BGM: fal ElevenLabs Music instrumental. SFX: procedural, per the `sfx:` cues; workers add no `<audio>`.

