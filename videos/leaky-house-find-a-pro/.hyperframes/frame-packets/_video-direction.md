## Video direction

**Canvas.** 1440×1080 (4:3). Every frame ground sets `container-type: size`; size everything in `cqw`/`cqh`. Full-bleed grounds ride on their own `class="clip"` background layer, never on `#root`.

**Cast (shared, never redraw).** The characters are pre-drawn SVGs in `public/characters/` — always place them with `<img src="../../public/characters/<file>.svg">` (path relative to `compositions/frames/`), never re-author them:
- `housy-neutral.svg` / `housy-sleep.svg` / `housy-worried.svg` / `housy-confused.svg` / `housy-happy.svg` — **小房子 Housy**, the protagonist (peach body, coral roof, butter chimney). viewBox 300×340. An expression change = stack two `<img>` of the same size at the same spot and hard-swap opacity (`tl.set`), with a tiny squash (scaleY 0.94 → 1) on the swap.
- `neighbor.svg` — the neighbor house (mint body, lavender arched roof, daisy). viewBox 300×340.
- `pro.svg` — the roofer pro (butter cap, sky overalls, coral toolbox, check-mark badge). viewBox 300×360.
Housy's standard size is ~26cqw wide unless a Scene says otherwise; keep his feet on an implied ground line. Props (bucket, drops, tools, phone, receipt, ladder, sun, stars) are drawn inline as SVG in the same style: 3px-equivalent charcoal `#2D2D2D` outlines (use stroke-width ≈ 0.42cqw-equivalent in SVG units), flat pastel fills, rounded joins.

**Palette.** From `frame.md` only: cream ground for data-dense frames; one saturated pastel ground per step frame, rotating butter → mint → sky → lavender → turquoise; white cards with 3px charcoal border + hard 6px offset shadow (no blur); coral only for small markers (step circles, drops of emphasis, the check mark ring). No gradients, no glow, no blur shadows.

**Type.** Chinese display and all Chinese text: `"ZCOOL KuaiLe"` (fallback `"Fredoka One", "Fredoka"`). Latin display + numerals: `"Fredoka"` weight 600 (stack `"Fredoka One", "Fredoka"`). Latin body/meta: `"Quicksand"` 600. Load Fredoka, Quicksand and ZCOOL KuaiLe from Google Fonts via a `<link>` in each frame. Numbers use `font-variant-numeric: tabular-nums`. Floor 1.4cqw for anything load-bearing.

**Shared step chrome (frames 3–7).** Top-left butter **badge-pill** at ~(3cqw, 3cqh): a coral circle-marker with the white step numeral + Fredoka/ZCOOL label, e.g. `STEP 1 · 自己修？`. Same position, same size in every step frame — the consistent stage. The step frame layout is: Housy in the left ~40%, the one white data card in the right ~55%, ornaments at corners.

**Subtitle band (every frame, fixed component — identical in all nine).** No voiceover exists; the bilingual subtitle IS the narration. Bottom band: a white pill centered horizontally, its top edge at 85cqh, max-width 86cqw, padding ~1.4cqw 3cqw, 3px charcoal border, 4px hard offset shadow, radius 50px. Line 1 Chinese in ZCOOL KuaiLe, 3.3cqw, `#2D2D2D`. Line 2 English in Quicksand 600, 1.75cqw, `#6B6B6B`. It enters at +0.25s with a short rise (y 1.2cqh → 0, opacity 0 → 1, power3.out, 0.35s) and then stays. When a frame lists two subtitle lines, the second replaces the first by hard swap at the stated time. All other content plans into the top ~83%.

**Ornaments.** 3–5 hand-drawn SVG ornaments per frame (daisy, star, cloud, sun, sparkle) at corners, cropping past the edge, behind content — per `frame.md`. Fewer (2–3) on the data-dense frames.

**Motion grammar.** One paused GSAP timeline per frame. Entrances are `fromTo`, smooth long-tail `power3.out`; this is a playful cartoon, so character and sticker pops may use a gentle `back.out(1.4)` — the only sanctioned overshoot, never on text or cards. Reveal each piece on its subtitle cue; never front-load. During holds, only a subtle low-amplitude jitter on Housy (≤0.4cqw, finite) or live SVG internals (drips, ringing lines). No breathing loops, no slow back-half pans, no `repeat:-1`, no `Math.random`.

**Rhythm.** Frame 1 is fast and comic; frame 2 is the one number-heavy stakes beat; frames 3–7 are the five-step run, one push-slide LEFT between each so they read as one journey; frame 8 is the calm breather (held, sunrise); frame 9 lands the thesis and holds to the end with the only real exit (a short fade of the whole frame in the last 0.4s).

**Negative list.** No stock photo look, no purple-blue AI gradients, no bokeh, no square corners, no blurred shadows, no fake browser/app chrome, no invented numbers (every figure below traces to HIRI and to `capture/extracted/visible-text.txt`), no slideshow (front-load then freeze), no screensaver (everything floating).

**Audio.** `music: none` here because HeyGen is signed out and local MusicGen is missing; the orchestrator synthesizes BGM + SFX procedurally and mounts them at the root after assembly. Workers never add `<audio>`. The `sfx:` lines below are the cue sheet for that synthesis.

