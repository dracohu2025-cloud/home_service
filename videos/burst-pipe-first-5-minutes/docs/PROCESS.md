# Process — Pipe Burst? Your First 5 Minutes

English 16:9 know-how for YouTube / Facebook / X。HyperFrames `faceless-explainer`，automation，直出 MP4。

完整时间线：[`../../docs/TIMELINE.md`](../../docs/TIMELINE.md)。选题动机：[`../../docs/TOPIC_SELECTION.md`](../../docs/TOPIC_SELECTION.md) §4–5。

## Inputs

| Doc | Role |
|---|---|
| `BRIEF.md` | Intent、事实、customizations |
| `SCRIPT.md` | 全英文 VO |
| `STORYBOARD.md` / `.hyperframes/frame-packets/` | 分镜与子任务包 |
| `compositions/frames/*.html` | 9 帧 GSAP |
| `frame.md` | blue-professional |
| `assets/` | 插画、音频、字幕 |

## Pipeline（实际跑通的顺序）

1. Brief + script — 锁定 Triple-I / Red Cross 事实；跳过争议「1/8-inch = 250 gal/day」  
2. `node scripts/make-illustrations.mjs`  
3. `python3 scripts/make-voice.py` — MiniMax `speech-2.8-hd` / `English_expressive_narrator`，bitrate 128000，词级时间；Whisper 漂移时对齐脚本（如 “2am.”）  
4. **BGM**：`python3 scripts/make-bgm-fal.py`（**不要**用已 410 的 `make-bgm.py` / MiniMax music-3.0-free）  
5. `python3 scripts/make-sfx.py`  
6. 9 帧 compose（旁白约 1.15×，元素卡词出现）  
7. 逐词字幕  
8. Render → `renders/pipe-burst-first-5-minutes.mp4`  
9. QA → [`QA.md`](QA.md) / [`CHANGELOG.md`](CHANGELOG.md)

## 用户五条意见如何落实

| # | 要求 | 落实 |
|---|---|---|
| 1 | YT/FB/X | 16:9 1920×1080；大号逐词字幕 |
| 2 | 真 know-how | 五步顺序 + 今日 CTA（给总阀贴标签） |
| 3 | 全英文 | MiniMax 英旁白 + 字幕 |
| 4 | 更高级 | 暖白 + 钴蓝线稿；无卡片阴影；Space Grotesk/Inter |
| 5 | 更活泼 | 1.15× VO；120 BPM BGM；~50 SFX；管中水持续动 |

## Environment

```bash
set -a; source /path/to/book-space-time/.env; set +a
# MiniMax 也可能来自 ~/.mmx
```

勿提交密钥。
