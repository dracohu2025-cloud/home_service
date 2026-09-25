# Home-service know-how videos

Explainer videos for US home-service / DIFM audiences。HyperFrames `faceless-explainer` + MiniMax TTS + 程序化/ fal 音频。

| Project | Language | Aspect | Length | Deliverable |
|---|---|---|---|---|
| [`leaky-house-find-a-pro/`](leaky-house-find-a-pro/) | zh on-screen (no VO) | 4:3 | ~60s | `renders/video.mp4` |
| [`burst-pipe-first-5-minutes/`](burst-pipe-first-5-minutes/) | en VO + captions + BGM | 16:9 | ~85s | `renders/pipe-burst-first-5-minutes.mp4` |

## 完整过程（给接手 Agent）

按这个顺序读：

1. [`AGENT_HANDOFF.md`](AGENT_HANDOFF.md) — 总图  
2. [`docs/TIMELINE.md`](docs/TIMELINE.md) — 时序  
3. [`docs/HIRI_RESEARCH.md`](docs/HIRI_RESEARCH.md) — **完整调研**  
4. [`docs/TOPIC_SELECTION.md`](docs/TOPIC_SELECTION.md) — 选题与换题  
5. [`docs/GSAP_SVG_PITFALLS.md`](docs/GSAP_SVG_PITFALLS.md) — 渲染前必读  
6. 各项目 `docs/PROCESS.md` / `QA.md` / `CHANGELOG.md`

## Secrets（永不提交）

运行时读 sibling `book-space-time/.env` 与 `~/.mmx`：

- `MINIMAX_API_KEY` — TTS  
- `FAL_API_KEY` — BGM（MiniMax music-3.0-free 已 410）
