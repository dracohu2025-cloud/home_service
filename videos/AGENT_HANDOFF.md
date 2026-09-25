# Agent handoff — home_service video exploration

This document captures the full process from HIRI topic research through two shipped HyperFrames videos, visual QA, and prevention rules. Goal: another agent can continue without re-discovering the same dead ends.

## 1. Research context (HIRI / DIFM)

- No public “HIRI US home-service Top 100 questions” list was found.
- Public DIFM / Project Decision themes that informed topics: water damage urgency, finding a pro, cost anxiety, “what do I do first.”
- Chosen topics:
  1. **Chinese**: leaky house → find a licensed pro (cartoon / daisy-days feel).
  2. **English**: pipe burst — first 5 minutes (premium / blue-professional, YouTube/Facebook/X).

## 2. Repo layout

```
home_service/
  videos/
    README.md                 ← index
    AGENT_HANDOFF.md          ← this file
    docs/GSAP_SVG_PITFALLS.md ← must-read before editing frame HTML
    leaky-house-find-a-pro/   ← Video A (zh, 4:3, no VO)
    burst-pipe-first-5-minutes/ ← Video B (en, 16:9, VO+captions+BGM)
```

Remote: `dracohu2025-cloud/home_service` on branch `main`.

## 3. Stack & APIs

| Piece | Choice | Notes |
|---|---|---|
| Motion | HyperFrames + GSAP in frame HTML | Seek-safe timelines; prefer SVG `rotate(cx,cy)` over GSAP rotation for clock hands |
| Style A | daisy-days preset | Cartoon leaky house |
| Style B | blue-professional | Cobalt line-art, Space Grotesk + Inter (avoid Fredoka One — lint) |
| TTS | MiniMax `speech-2.8-hd`, voice `English_expressive_narrator` | Bitrate 128000; word timings for captions |
| BGM | **fal** ElevenLabs Music | MiniMax `music-3.0-free` → **HTTP 410 Gone**. Script: `scripts/make-bgm-fal.py` |
| SFX | Procedural Python (`make-sfx.py`) | Water, dial, click, etc. |
| Captions | Word-timed from TTS meta | Whisper sometimes mangles “2am.” — align to script words |
| Keys | `book-space-time/.env` + `~/.mmx` | Never commit `.env*` |

## 4. Video A — leaky-house-find-a-pro

- Path: `videos/leaky-house-find-a-pro/`
- ~60s, 4:3, Chinese on-screen text, no narration.
- Automation flow, no storyboard gate.
- Deliverable: `renders/video.mp4`
- Process notes: `docs/PROCESS.md`

## 5. Video B — burst-pipe-first-5-minutes

- Path: `videos/burst-pipe-first-5-minutes/`
- ~84.8s, 1920×1080, English VO + captions + BGM + SFX.
- Message: five calm moves — valve → power → drain → document → call; CTA: find & tag main shut-off today.
- Deliverable: `renders/pipe-burst-first-5-minutes.mp4`
- Rebuild scripts under `scripts/`; pipeline notes in `docs/PROCESS.md`
- Visual QA: `docs/QA.md` + contact sheets in `docs/qa-sheets/`

### Scene order (high level)

1. Hook — pipe burst / urgency + $15,400 claim stat  
2. Step 1 — shut main valve (gate vs ball)  
3. Step 2 — power only if dry path  
4. Step 3 — drain lines / water heater  
5. Step 4 — document damage  
6. Step 5 — call plumber + insurer  
7. CTA — tag the valve today  

Facts cited in `BRIEF.md` (Triple-I / Red Cross / Forbes Home). Deliberately avoided disputed “1/8-inch = 250 gal/day” claim.

## 6. Bugs that shipped once (must not repeat)

### 6.1 Clock hands misaligned (user-reported)

- **Cause**: GSAP `fromTo` with **asymmetric** `svgOrigin` / `transformOrigin` between from-vars and to-vars. Under seek/render, the pivot jumps.
- **Fix**: Prefer native SVG `transform="rotate(angle cx cy)"` on hands, or ensure from/to origins are identical.
- **Prevention**: `scripts/qa-scan.py` flag A (origin asymmetry). Auto-patched 18 asymmetries → 0.

### 6.2 Blue “drip” scene incomprehensible (user-reported)

- **Cause**: Abstract drip + GSAP `x/y/rotation` on SVG nodes that already had `transform="..."` attributes → GSAP **clobbers** the attribute transform.
- **Fix**: Rewrote as pipe + crack + drops; wrap animated nodes in `<g>` without competing `transform`; animate the group.
- **Prevention**: `qa-scan.py` flags B (transform clobber) and C (rotate without origin).

### 6.3 Other polish

- Faucet tilt 50° → 35° (less extreme).
- Font: dropped Fredoka One; Space Grotesk + Inter.

## 7. QA process used

1. Static: `python3 scripts/qa-scan.py` on all `compositions/frames/*.html`
2. Dense visual: extract frames every **0.5s** from final MP4 → montage contact sheets (`docs/qa-sheets/sheet-00.png` … `sheet-14.png`, ~184 frames total in original `/tmp` run)
3. Human/agent review of sheets for: empty beats, overlapping text, broken pivots, illegible icons, caption collisions

When changing any frame HTML, re-run qa-scan before re-render. After re-render, spot-check new dense sheets or at least mid-point snapshots already in the project.

## 8. How to rebuild Video B (sketch)

From `videos/burst-pipe-first-5-minutes/` (exact HyperFrames CLI may vary by installed version):

```bash
# Voice (needs MINIMAX_API_KEY)
python3 scripts/make-voice.py

# BGM via fal (needs FAL_API_KEY) — do NOT use retired MiniMax music-3.0-free
python3 scripts/make-bgm-fal.py

# SFX
python3 scripts/make-sfx.py

# Illustrations if regenerating assets
node scripts/make-illustrations.mjs

# Then HyperFrames compose + render per project BRIEF / frame.md
# Finally:
python3 scripts/qa-scan.py
```

Keys: load from `../../book-space-time/.env` or export from `~/.mmx` — see script headers.

## 9. What was intentionally not committed

- Raw per-frame PNGs under `/tmp/pipe-test/qa/` (~184 files) — **contact sheets only** are in-repo.
- One-off throwaway fix scripts that lived only in `/tmp` — logic preserved in `docs/QA.md` and `qa-scan.py`.
- API keys / `.env` files.

## 10. Suggested next work for a following agent

- Apply `qa-scan.py` (or extract it) to Video A frames.
- Package a shared `videos/scripts/qa-scan.py` used by both projects.
- Optional: Cursor rule pointing at `docs/GSAP_SVG_PITFALLS.md` for any SVG/GSAP edit.
- Platform export variants (square / vertical) from the 16:9 master if needed for X/Reels.
- BGM volume ducking vs VO if platform mixes feel loud.

## 11. Key commit history (this repo)

- Initial research / Video A + Video B deliverables and mid QA snapshots were committed earlier on `main`.
- Follow-up commit(s) add this handoff doc set, dense QA contact sheets, and process/QA writeups so the **full process** is recoverable from git alone.
