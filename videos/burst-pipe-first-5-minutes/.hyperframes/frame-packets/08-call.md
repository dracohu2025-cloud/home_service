# Frame packet: 08-call

## Project inputs

- Project: /Users/dracohu/REPO/home_service/videos/burst-pipe-first-5-minutes
- Design tokens: /Users/dracohu/REPO/home_service/videos/burst-pipe-first-5-minutes/frame.md
- RULES_DIR: /Users/dracohu/.agents/skills/hyperframes-animation/rules

## Assigned storyboard block

## Frame 8 — Step 5 · Call the pros

- scene: two cards — licensed plumber and insurance company; then a crossed-out tape roll: tape won't hold at full pressure
- voiceover: "Five. Call the pros: a licensed plumber for the repair, and your insurance company to start the claim. And skip the tape. It won't hold against full water pressure."
- tag: STEP 5 · CALL
- duration: 9.88s
- poster: 9.5s
- transition_in: push-slide LEFT
- status: outline
- src: compositions/frames/08-call.html
- type: feature_showcase
- persuasion: Comparison of two roles + myth-busting
- beat: confidence + resolve
- blueprint: comparison-split (Adapt)
- focal: the two pro cards
- roles: step column = foreground · stage: two tinted cards side by side (wrench / shield) = foreground hero · tape-no strip = supporting
- sfx: whoosh at 0.1s; card-whoosh at 2.16s and 4.1s; chime at 5.4s; buzz at 6.63s

narrativeRole: Fifth move — hand off to the right people, and kill the most common bad fix.
keyMessage: Call a licensed plumber and your insurer; tape is not a fix.

Adapt: keep the paired-cards-from-opposite-sides entrance, with a gentle mirrored tilt that settles flat (no 3D wobble), then a strip below.
Scene 1 (0.0–2.1s): step-circle "5", eyebrow `STEP 05 / 05`, h2 "Call the pros" (1.00s).
Scene 2 (2.1–5.9s): card A enters from the left on "licensed" (2.16s): `wrench.svg` + title "Licensed plumber" + muted "for the repair"; card B enters from the right on "insurance" (4.10s): `shield-check.svg` + "Your insurer" + "to start the claim"; on "claim" (5.37s) the shield's `#check` draws in green.
Scene 3 (5.9–9.88s): on "skip" (6.19s) a wide split-highlight strip with a RED left rule slides in under the cards: `tape-no.svg` small + "Skip the tape — it won't hold at full pressure." Hold.

## Selected blueprint: comparison-split

# comparison-split — Comparison Split-Cards

**intent**: Two paired items of equal weight shown side-by-side with mirrored 3D "book-open" tilts — the eye reads them as a balanced comparison, then a pill badge lands at each card's inner edge to punctuate. The motion IS the symmetry: two cards arriving from opposite wings into a held spread.

**roles served**

- Key_Feature (from `comparison-split-cards`): when two complementary features / capabilities of equal weight should be presented **simultaneously, not sequentially** — an A/B, a "X + Y together," paired concepts the viewer must weigh side-by-side. Not for >2 items (use `grid-card-assemble`) or sequential steps.

**duration**: 4–6s

**shot structure** (a `[bg]` canvas carrying two faint ambient glow blooms — `[accent A]` near 30%, `[accent B]` near 70% — so each side owns a color identity across a 50% symmetry axis; equal-width cards under one shared perspective parent)

- **Scene 1 (0.0–~0.8s) — title sets the concept.** A centered `[title line]` with an `[accent keyword]` slides DOWN into place from just above (a short smooth settle). The downward arrival is deliberate: it forms a non-conflicting T-shape against the cards, which arrive from the sides next.
- **Scene 2 (~0.4–1.9s) — the split-tilt entry (signature move).** Two equal-width feature cards arrive from opposite wings — `[left card]` from the left, `[right card]` from the right ~0.2s behind — each carrying a **mirrored 3D `rotateY` tilt** (left faces right, right faces left, opening like a book) and scaling ~0.85→1 as it lands. The entry overlaps the title's tail so the whole thing reads as ONE arrival, not two beats. Each card holds `[image / label / subtitle]`; box-shadows fall **outward** from the tilt (left shadow right, right shadow left).
- **Scene 3 (~1.9–end) — badges punctuate, then hold.** A pill `[badge]` lands at each card's **inner edge** (left then right, ~0.3s apart), overlapping its card ~15% so it reads as attached, not orbiting. This is the lone overshoot in the shot — it earns the punctuation. Settles and holds.

**motion vocabulary**: title slide-down from above; mirrored opposite-wing card entry; static book-open `rotateY` tilt (`+tilt` left, `−tilt` right); tilt-matched outward box-shadow; inner-edge badge spring-pop; gentle phase-opposed idle float (left vs right, never synchronized) registered as subtle jitter; dual side-glow ambient.

**rule mapping**

- two cards entering from opposite wings with mirrored `rotateY` tilts + tilt-matched shadow → `split-tilt-cards` (the signature; keep the two-layer split so the entry `x`/`scale` and the idle never collide on one alias)
- title slide-down settle → `gsap-effects` (translate + opacity on a long-tail `power3`)
- inner-edge pill badge pop (the one overshoot) → `spring-pop-entrance` (overshoot register — earns the punctuation)
- phase-opposed idle float on the pair → `sine-wave-loop` (low-amplitude register — subtle jitter, NOT lazy breathing; left `sin(t)`, right `sin(t+π)` so they never conveyor-belt)
- the two faint side glows behind the cards → `ambient-glow-bloom` (un-triggered soft bloom, one per accent)

**camera modifier**: camera-static by default — the symmetry is the subject and a move would break the balance.
