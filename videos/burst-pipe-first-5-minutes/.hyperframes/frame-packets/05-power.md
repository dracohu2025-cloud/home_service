# Frame packet: 05-power

## Project inputs

- Project: /Users/dracohu/REPO/home_service/videos/burst-pipe-first-5-minutes
- Design tokens: /Users/dracohu/REPO/home_service/videos/burst-pipe-first-5-minutes/frame.md
- RULES_DIR: /Users/dracohu/.agents/skills/hyperframes-animation/rules

## Assigned storyboard block

## Frame 5 — Step 2 · Cut the power, safely

- scene: a breaker panel; the affected switch flips off; a red-ruled warning says never stand in water; fallback: call an electrician
- voiceover: "Two. Kill the power, safely. If water is near outlets or appliances, switch that area off at the breaker. But never stand in water to reach the panel. If you can't get there dry, call an electrician."
- tag: STEP 2 · POWER
- duration: 12.11s
- poster: 11.7s
- transition_in: push-slide LEFT
- status: outline
- src: compositions/frames/05-power.html
- type: feature_showcase
- persuasion: Signposting + counterexample (the dangerous way)
- beat: caution + clarity
- blueprint: compose
- focal: the breaker toggle flipping off, then the danger rule
- roles: step column = foreground · right stage: `breaker-panel.svg` large = foreground hero · a small outlet icon with water drops (inline SVG in the kit style) = supporting · warning split-highlight (4px RED left rule) = foreground in Scene 3
- sfx: whoosh at 0.1s; pop at 2.7s; breaker-click at 6.33s; warn-tone at 7.06s; pop at 9.4s

narrativeRole: Second move — remove the electrocution risk, without creating a new one.
keyMessage: Switch off the affected area at the breaker — but only if you can reach it dry; otherwise call an electrician.

Scene 1 (0.0–2.6s): step-circle "2", eyebrow `STEP 02 / 05`, h2 "Cut the power — safely" (0.79s). Stage card: `breaker-panel.svg` centered.
Scene 2 (2.6–6.9s): on "outlets" (3.49s) a small outlet glyph with two cobalt drops appears at the stage's lower-left with a red hairline zigzag; row chip 1 "Water near outlets or appliances?" (2.66s). On "switch" (5.26s) the red `#switch-target` frame pulses; on "breaker" (6.33s) `#switch-toggle` slides to OFF (power2.inOut 0.25s), turns muted, a tiny green check appears beside it; row chip 2 "Switch that area off at the breaker" (5.26s).
Scene 3 (6.9–9.3s): on "never" (7.06s) a split-highlight card with a 4px RED left rule slides in over the lower left column: bold near-black "Never stand in water to reach the panel." with a small red warning glyph; the outlet glyph's zigzag flickers once.
Scene 4 (9.3–12.11s): on "If you can't" (9.38s) a final chip "Can't reach it dry? → Call an electrician" reveals; hold.
