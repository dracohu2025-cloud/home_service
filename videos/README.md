# Home-service know-how videos

Explainer videos for US home-service / DIFM audiences (HIRI-informed topics). Built with **HyperFrames** `faceless-explainer` workflow, MiniMax TTS, and programmatic SVG motion.

| Project | Language | Aspect | Length | Deliverable |
|---|---|---|---|---|
| [`leaky-house-find-a-pro/`](leaky-house-find-a-pro/) | zh (on-screen only, no VO) | 4:3 | ~60s | `renders/video.mp4` |
| [`burst-pipe-first-5-minutes/`](burst-pipe-first-5-minutes/) | en + MiniMax VO + captions + BGM | 16:9 | ~85s | `renders/pipe-burst-first-5-minutes.mp4` |

## Agent handoff

Start here if continuing this work:

1. **[`AGENT_HANDOFF.md`](AGENT_HANDOFF.md)** — full exploration history, API keys, stack choices, bugs found, and how to reproduce/rebuild.
2. **[`docs/GSAP_SVG_PITFALLS.md`](docs/GSAP_SVG_PITFALLS.md)** — the two SVG/GSAP bugs that bit us (clock hands + drip) and the QA gate that prevents them.
3. Per-project: `BRIEF.md`, `STORYBOARD.md`, `docs/PROCESS.md`, `docs/QA.md` (English video only).

## Secrets (never commit)

Runtime keys are read from sibling repo `book-space-time/.env` and `~/.mmx`. Do **not** put API keys in this repo.

- `MINIMAX_API_KEY` — TTS (`speech-2.8-hd`)
- `FAL_API_KEY` — BGM via fal ElevenLabs Music (MiniMax `music-3.0-free` is retired HTTP 410)
