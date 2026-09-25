# Process — 漏水找师傅 (leaky-house-find-a-pro)

Chinese 4:3 faceless explainer, ~60s, **no voiceover** (on-screen copy only). First HyperFrames cut in this repo; later superseded in *style* by the English premium pipe-burst video, but kept as the Mandarin / square-ish deliverable.

## Intent

Cartoon / daisy-days house with a leak → calm path to finding a licensed pro. Automation flow, no storyboard review gate. Direct MP4.

## Layout

| Path | Role |
|---|---|
| `BRIEF.md` | Intent + constraints |
| `STORYBOARD.md` | Beats |
| `compositions/` | Frame HTML + characters |
| `synth-audio/` | Any bed / SFX used |
| `renders/video.mp4` | Final |

## Lessons carried into Video B

- Daisy-days reads “cute” — fine for zh short; English social ask needed **blue-professional**, livelier motion, real VO.
- Always plan a visual QA pass (see sibling project `docs/QA.md` and repo `videos/docs/GSAP_SVG_PITFALLS.md`).
- Prefer committing process docs + contact sheets with the MP4 so later agents inherit context.

## Suggested follow-up

- Run the same `qa-scan.py` origin/clobber checks on this project’s frame HTML.
- Optional: English export or vertical crop if needed; otherwise leave as zh reference cut.
