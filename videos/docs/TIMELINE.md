# 项目时间线（完整过程）

按真实对话顺序整理，便于后续 Agent 复盘。本地对话记录：Cursor agent transcript `d42cc8a3-37e2-4dba-9eff-5dc6817665fc`。

| 时间 (UTC+8) | 阶段 | 做了什么 | 产物 / 仓库位置 |
|---|---|---|---|
| 2026-09-24 22:45 | 调研 | 检索 HIRI「Top 100」；确认无公开清单；整理 DIFM / Project Decision 公开结论 | [`HIRI_RESEARCH.md`](HIRI_RESEARCH.md) |
| 2026-09-24 23:01 | 选题 | 分析 X 参考视频；提出 5 个方案；推荐方案二 | [`TOPIC_SELECTION.md`](TOPIC_SELECTION.md) |
| 2026-09-24 夜 | Video A 制作 | HyperFrames faceless-explainer；9 帧并行；程序化音频；渲染 4:3 中文无旁白片 | `leaky-house-find-a-pro/` → `renders/video.mp4` |
| 2026-09-24 23:25 | 交付 A | 告知成片路径；说明圆环计数中间帧可能误读 | 同上 |
| 2026-09-24 23:32 | 反馈 | 平台/科普/英文/高级感/节奏；指向 book-space-time 密钥；允许换题 | — |
| 2026-09-24～25 | Video B 制作 | 新 BRIEF/SCRIPT；blue-professional；MiniMax TTS 1.15×；MiniMax music → **HTTP 410** → 改 fal ElevenLabs Music；9 帧 + 字幕 + SFX | `burst-pipe-first-5-minutes/` |
| 2026-09-25 ~06:xx | 交付 B | 84.8s 16:9 MP4；说明与预期差异（BGM 源、时长 85 vs 75） | `renders/pipe-burst-first-5-minutes.mp4` |
| 2026-09-25 ~06:53 | Bug 1 | 用户：时钟指针错位（附图） | `docs/feedback/01-clock-hands-misaligned.png` |
| 同日 | Fix 1 | svgOrigin 只在 to-vars；改为圆心固定旋转；重渲 | 见 `CHANGELOG.md` |
| 2026-09-25 ~06:59 | Bug 2 | 用户：蓝线是什么？（附图） | `docs/feedback/02-abstract-drip-incomprehensible.png` |
| 同日 | Fix 2 | 抽象滴水 → 可识别水管+裂口+水珠；重渲 | 见 `CHANGELOG.md` |
| 2026-09-25 07:42 | 全面 QA | 用户要求查同类瑕疵 + 预防总结 | `qa-scan.py`；密集 0.5s 截图 |
| 同日 | Fix 3 | 再修 17 处 origin 不对称 + 马桶漩涡无原点 + 水龙头 50°→35°；TOTAL 0 | `docs/QA.md`、`docs/qa-sheets/` |
| 2026-09-25 07:50 | 首次 push | 成片与脚本进仓（过程文档尚不全） | commit `d906c6a` |
| 2026-09-25 10:13+ | 过程归档 | 用户确认过程未全交；补 handoff / QA sheets / Cursor 规则 | `10dcf38`、`2ac9eef` |
| 2026-09-25 10:25+ | 完整过程 | 补全 HIRI 全文、选题、时间线、修复 changelog、用户反馈图 | 本轮 commit |

## 密钥约定（从未入库）

运行时从 `book-space-time/.env` 与 `~/.mmx` 读取：`MINIMAX_API_KEY`、`FAL_API_KEY`。仓库内无 `.env`。
