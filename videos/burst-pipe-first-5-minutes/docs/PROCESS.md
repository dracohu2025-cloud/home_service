# Process — Pipe Burst? Your First 5 Minutes

English 16:9 know-how explainer for YouTube / Facebook / X. HyperFrames `faceless-explainer`, automation flow, direct MP4.

## Inputs

| Doc | Role |
|---|---|
| `BRIEF.md` | Intent, facts, customizations |
| `SCRIPT.md` | Full VO script |
| `STORYBOARD.md` | Beat / visual map |
| `compositions/frames/*.html` | Per-scene GSAP compositions |
| `compositions/frame.md` | blue-professional preset notes |
| `assets/` | Illustrations, audio, captions |

## Pipeline (order that worked)

1. **Brief + script** — lock facts (Triple-I $15,400; Red Cross power guidance). Skip disputed leak-rate claim.
2. **Illustrations** — `node scripts/make-illustrations.mjs` (cobalt line-art house, valve, breaker, etc.).
3. **Voice** — `python3 scripts/make-voice.py`  
   - MiniMax `speech-2.8-hd` / `English_expressive_narrator`  
   - bitrate `128000`  
   - persist word timings in `audio_meta` for captions  
   - if Whisper alignment drifts (e.g. “2am.”), force-align to script tokens
4. **BGM** — `python3 scripts/make-bgm-fal.py`  
   - **Not** MiniMax music (`music-3.0-free` returns HTTP 410)  
   - fal ElevenLabs Music via `FAL_API_KEY` from book-space-time `.env`
5. **SFX** — `python3 scripts/make-sfx.py` (procedural)
6. **Compose frames** — HyperFrames + blue-professional; Space Grotesk + Inter only
7. **Captions** — word-timed burn-in / sidecar from TTS meta
8. **Render** → `renders/pipe-burst-first-5-minutes.mp4` (~84.8s, 1920×1080)
9. **QA** — see `QA.md`

## Environment

```bash
# Typical: source sibling env
set -a; source /Users/dracohu/REPO/book-space-time/.env; set +a
# or keys from ~/.mmx for MiniMax
```

Never commit secrets. `.gitignore` covers `.env*`, `node_modules`, `.DS_Store`.

## Style constraints (from user feedback)

- Premium, not cheap/cartoony (moved away from daisy-days).
- Livelier pacing; upbeat BGM under VO.
- English only for this cut; platforms: YT / FB / X.
- First Chinese 4:3 cut lives in sibling folder `../leaky-house-find-a-pro/`.
