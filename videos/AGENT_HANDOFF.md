# Agent handoff — home_service 视频探索

后续 Agent **先读索引，再按需下钻**。完整时间线见 [`docs/TIMELINE.md`](docs/TIMELINE.md)。

## 文档地图

| 文档 | 内容 |
|---|---|
| [`docs/HIRI_RESEARCH.md`](docs/HIRI_RESEARCH.md) | **完整** HIRI/DIFM 调研（无公开 Top 100；公开结论与来源链接） |
| [`docs/TOPIC_SELECTION.md`](docs/TOPIC_SELECTION.md) | 5 方案、参考 X 帖、Video A/B 选题决策 |
| [`docs/TIMELINE.md`](docs/TIMELINE.md) | 从调研到 push 的时序 |
| [`docs/GSAP_SVG_PITFALLS.md`](docs/GSAP_SVG_PITFALLS.md) | SVG/GSAP 两类硬伤 + 门禁 |
| [`burst-pipe-first-5-minutes/docs/PROCESS.md`](burst-pipe-first-5-minutes/docs/PROCESS.md) | 英文片制作流水线 |
| [`burst-pipe-first-5-minutes/docs/QA.md`](burst-pipe-first-5-minutes/docs/QA.md) | QA 门禁与 checklist |
| [`burst-pipe-first-5-minutes/docs/CHANGELOG.md`](burst-pipe-first-5-minutes/docs/CHANGELOG.md) | 用户反馈 → 根因 → 修复 → 验证 |
| [`burst-pipe-first-5-minutes/docs/feedback/`](burst-pipe-first-5-minutes/docs/feedback/) | 用户原图（时钟 / 蓝线） |
| [`burst-pipe-first-5-minutes/docs/qa-sheets/`](burst-pipe-first-5-minutes/docs/qa-sheets/) | 0.5s 密集质检联系表 ×15 |
| [`leaky-house-find-a-pro/docs/PROCESS.md`](leaky-house-find-a-pro/docs/PROCESS.md) | 中文卡通片过程 |

## 两个成片

| | Video A | Video B |
|---|---|---|
| 路径 | `leaky-house-find-a-pro/` | `burst-pipe-first-5-minutes/` |
| 语言 | 中英字幕，无 VO | 英文 MiniMax VO + 字幕 |
| 画幅 | 4:3 ~60s | 16:9 ~84.8s |
| 风格 | daisy-days 卡通 | blue-professional |
| MP4 | `renders/video.mp4` | `renders/pipe-burst-first-5-minutes.mp4` |

远程：`dracohu2025-cloud/home_service`，分支 `main`。

## Stack 速查

| 片 | 选择 | 注意 |
|---|---|---|
| 运动 | HyperFrames + GSAP | seek-safe；时钟优先 SVG `rotate(cx,cy)` |
| TTS | MiniMax speech-2.8-hd | `English_expressive_narrator`；bitrate 128000 |
| BGM | **fal** ElevenLabs Music | MiniMax music-3.0-free → **HTTP 410** |
| SFX | 程序化 Python | |
| 密钥 | book-space-time `.env` + `~/.mmx` | **永不提交** |

## 必跑门禁（改帧后）

```bash
cd videos/burst-pipe-first-5-minutes
python3 scripts/qa-scan.py   # TOTAL 0
npm run check
# 重渲后建议 0.5s 联系表目检
```

## 刻意未入库

- `/tmp` 下原始 169 张单帧 PNG（联系表已入库）  
- API keys / `.env`  
- 修复前中间 MP4 二进制历史（叙事在 CHANGELOG；git 只有终态为主）

## 建议下一步

- 把 `qa-scan.py` 抽到 `videos/scripts/` 供两项目共用  
- Video A 跑同源扫描  
- 需要时做竖版/方版从 16:9 master 裁切  
- BGM 相对 VO 的 ducking
