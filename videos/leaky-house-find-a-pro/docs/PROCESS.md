# Process — 漏水找师傅 (leaky-house-find-a-pro)

Video A：中文 4:3、~60s、**无旁白**（烧录中英字幕）。数据与叙事来自 [`../../docs/HIRI_RESEARCH.md`](../../docs/HIRI_RESEARCH.md) 与 [`../../docs/TOPIC_SELECTION.md`](../../docs/TOPIC_SELECTION.md) 方案二。

## 规格

| 项 | 值 |
|---|---|
| 画幅 | 1440×1080（4:3） |
| 时长 | ~60s |
| 风格 | daisy-days / 卡通方块房 Housy |
| 音频 | 程序化 BGM + SFX（当时 HeyGen 未登、本地 MusicGen 缺依赖） |
| 成片 | `renders/video.mp4` |

## 结构

| Path | Role |
|---|---|
| `BRIEF.md` | 意图 + HIRI 数据点 |
| `STORYBOARD.md` / frame-packets | 9 拍 |
| `compositions/frames/` | 并行子任务 HTML |
| `scripts/synth-audio.py` 等 | 音频 |
| `capture/extracted/visible-text.txt` | 需求与数据原文快照 |

## 制作要点

- 9 帧并行写 GSAP，再拼主时间轴。  
- 数字滚动；每步 HIRI 数据卡。  
- 曾提醒：第 5 帧圆环计数中间可能闪「0/3」「1/3」（动画插值，非真实数据）。

## 为何有 Video B

用户反馈：要发 FB/YT/X、真 know-how、全英文、更高级、更欢快 → 换题做 `../burst-pipe-first-5-minutes/`（见 TIMELINE）。本片保留为中文卡通参考成片。

## 建议后续

对本项目帧 HTML 跑 sibling 的 `qa-scan.py` 同源/clobber 检查。
