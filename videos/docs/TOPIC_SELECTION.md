# 选题过程

> 日期：2026-09-24 → 09-25  
> 前置：[`HIRI_RESEARCH.md`](HIRI_RESEARCH.md)

## 1. 用户目标（第一轮）

用 code2video / HyperFrames 做一条 know-how 视频。参考 X 上 Opus 5.5 风格成片（全部代码绘制，无视频生成模型）：

- https://x.com/akokoi1/status/2102950749240181000
- https://x.com/dashiAIxz/status/2103031723428917626
- https://x.com/NFT_Chen/status/2102681172367323300
- https://x.com/xiaohu/status/2102979455308439555
- https://x.com/Perseverance_ii/status/2102789098503299506
- 搜索入口：https://x.com/search?q=opus5.5&src=typed_query

参考视频画风大致三种：手绘纸面 + 信息卡；卡通小人 + 假剪辑软件 UI；手绘叙事 + 双语字幕；另有极简日历隐喻。

## 2. 五个候选方案（基于 HIRI 公开数据）

### 方案一：美国房主的一年（日历体）

- 手撕日历 1→12 月，每月一种上门服务。
- 数字滚动：$1,390 / $812 / $590 等。
- 开头：「美国房主一年要请几次师傅？」

### 方案二：小房子漏水了（卡通叙事）★ 第一轮采用

- 方块小房子半夜漏水 → 找师傅五步（缺技能工具 → 问邻居 → 电话约 → 报价不透明 → 挑口碑）。
- 每步弹出 HIRI 数据卡；中英双语字幕；无旁白。
- 开头：滴、滴、滴……

### 方案三：请美国师傅前必须知道的 5 件事（清单体）

- 方格纸 + 手绘信息卡。

### 方案四：一张年度维修收据（收据体）

- 热敏纸吐账单 + 插画。

### 方案五：美国人不再纯 DIY 了（反套路）

- DIY vs 请人拔河；纯 DIY 下降、混合上升。

**当时推荐**：方案二（传播力 + 知识点可串故事 + 最接近参考爆款）。

## 3. Video A 落地

- 目录：`videos/leaky-house-find-a-pro/`
- 规格：约 60s，1440×1080（4:3），daisy-days 卡通，程序化 BGM/SFX，无 TTS。
- 成片：`renders/video.mp4`

## 4. 用户第二轮反馈 → 换题重做

路径：`/Users/dracohu/REPO/book-space-time` 提供 MiniMax TTS / 音乐 / FAL 等密钥。

要求：

1. 发布到 Facebook / YouTube / X  
2. 真正的生活 know-how（看完能照做）  
3. 全英文（可加英文 TTS）  
4. 更精致、更高级（上一版偏 cheap）  
5. 节奏更欢快  

允许重新选题，直接出 MP4。

## 5. Video B 选题

**Pipe Burst? Your First 5 Minutes**

- 理由：紧急、可操作、顺序明确；比「行业洞察找师傅」更贴社交媒体科普。
- 数据锚点改用 Triple-I：约 1/67 参保住宅有水损/冰冻理赔，平均 $15,400（见 BRIEF）。
- 目录：`videos/burst-pipe-first-5-minutes/`
- 规格：~84.8s，1920×1080，blue-professional，MiniMax VO + 逐词字幕 + fal BGM + 程序化 SFX。

详见 [`TIMELINE.md`](TIMELINE.md) 与两项目 `docs/PROCESS.md`。
