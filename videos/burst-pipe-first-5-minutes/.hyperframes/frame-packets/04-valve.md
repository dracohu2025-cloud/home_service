# Frame packet: 04-valve

## Project inputs

- Project: /Users/dracohu/REPO/home_service/videos/burst-pipe-first-5-minutes
- Design tokens: /Users/dracohu/REPO/home_service/videos/burst-pipe-first-5-minutes/frame.md
- RULES_DIR: /Users/dracohu/.agents/skills/hyperframes-animation/rules

## Assigned storyboard block

## Frame 4 — Step 1 · Shut off the main valve

- scene: the cutaway highlights where the main valve lives, then a wheel valve turns clockwise and a lever valve turns a quarter turn across the pipe
- voiceover: "One. Shut off the main water valve. It's usually where the water line enters your home: the basement, a crawl space, a utility room, or near the water meter. A round wheel turns clockwise. A lever turns a quarter turn, until it sits across the pipe."
- tag: STEP 1 · VALVE
- duration: 15.24s
- poster: 14.8s
- transition_in: push-slide LEFT
- status: outline
- src: compositions/frames/04-valve.html
- type: feature_showcase
- persuasion: Signposting + demonstration
- beat: focus + "aha"
- blueprint: compose
- focal: the valve illustrations performing the turn
- roles: step column (left) = foreground · right tinted stage card: house cutaway, then gate valve, then ball valve = foreground hero · location chips = supporting
- sfx: whoosh at 0.1s; pop at 5.06, 5.76, 6.77, 7.91s; valve-turn 10.1–11.0s; valve-turn 12.1–13.0s; click at 13.9s

narrativeRole: The single most important move — stop the water at the source — with enough how-to that the viewer can actually do it.
keyMessage: Find the main valve where the line enters the house; wheel = clockwise, lever = quarter turn across the pipe.

Scene 1 (0.0–2.6s): step layout: step-circle "1", eyebrow `STEP 01 / 05`, h2 "Shut off the main water valve" (reveals on "Shut", 0.43s). Right stage card holds `house-cutaway.svg`, pipes flowing (live dash).
Scene 2 (2.6–9.2s): on "enters" (4.08s) `#pipe-main` glows cobalt and a pulsing cobalt ring marks `#valve-main`; location chips reveal under the h2 as each is named — "Basement" (5.06s), "Crawl space" (5.76s), "Utility room" (6.77s), "Near the water meter" (7.91s) — and on "meter" (8.80s) a second ring marks `#meter`.
Scene 3 (9.2–11.1s): at 9.2s the stage card swaps (velocity-matched scale cut) to a big `valve-gate.svg`; a label chip "Wheel → clockwise" with a curved cobalt arrow; on "clockwise" (10.41s) `#wheel` rotates clockwise 2 full turns (power2.inOut, ~0.9s) while a small flow dash in its pipe decelerates to a stop.
Scene 4 (11.1–15.24s): at 11.12s a second stage card slides in beside/over it with `valve-ball.svg`, lever along the pipe; label chip "Lever → ¼ turn"; on "quarter turn" (12.10s) `#lever` rotates 90° to sit across the pipe (power2.inOut, 0.6s); on "across" (13.87s) a green check + "OFF" pill appears on both valve cards. Hold.
