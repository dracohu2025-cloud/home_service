# Changelog — burst-pipe-first-5-minutes

记录成片落地后的用户反馈、根因、修复与验证。截图在 `feedback/`，密集质检拼图在 `qa-sheets/`。

## v1 — 初渲交付（~84.8s）

- 全英文 MiniMax `speech-2.8-hd` / `English_expressive_narrator`，旁白约 1.15×
- 逐词字幕；120 BPM BGM（**fal** ElevenLabs Music；MiniMax `music-3.0-free` 已 410）
- 程序化 SFX ~50 点；blue-professional；Space Grotesk + Inter
- 数据：Triple-I 1 in 67 / $15,400
- 粗检：每场景中点 1 张（后证明不够）

## v1.1 — 时钟指针错位

**用户**（附图 `feedback/01-clock-hands-misaligned.png`）：「第一张图里时钟的指针错位了」

**根因**：分针/时针的 `svgOrigin`（或等价旋转中心）只写在 `fromTo` 的 **to-vars**，from 侧缺失 → seek/渲染时绕错圆心。

**修复**：旋转中心固定在表盘圆心；优先 SVG `rotate(angle cx cy)` 或 from/to 同源。

**验证**：抽 0.4s / 1.5s / 3s / 4.5s，指针从圆心转到约 2:00，缩到左上角不偏。重渲同路径 MP4。

## v1.2 — 抽象「蓝线」滴水不可读

**用户**（附图 `feedback/02-abstract-drip-incomprehensible.png`）：「红色箭头所指的蓝色线段是啥意思？是放错位置了么？」

**根因**：不是放错位置，是**画得太抽象**（短横=天花水管，虚线=滴水），手机缩略不可辨。另有 GSAP 与 SVG `transform=` 冲突的风险类（见 `../../docs/GSAP_SVG_PITFALLS.md`）。

**修复**：第 7 帧手机屏内与飞出照片均改为「带接头水管 + 红裂口 + 逐滴水珠 + 积水」；水管避开取景框角标。

**验证**：重渲后目检 60.6s 一带画面。

## v1.3 — 全面同类扫描 + 密集目检

**用户**：「再检查是否还有刚才那种低级瑕疵，并总结如何预防。」

### 自动扫描 `scripts/qa-scan.py`

| 结果 | 说明 |
|---|---|
| 18 处命中 → 修到 0 | 17× origin 不对称（帧 1/2/4/5/9）；1× 马桶漩涡旋转无原点（帧 6） |
| lint 误报不改 | `#h01-burst-ring` 两段 fromTo 属性不重叠；`dwell/hold` 解析误报 |

辅助脚本：`scripts/fix-origin-asymmetry.py`（可 dry-run）。

### 密集目检

- 每 **0.5s** 一帧，约 **169** 张 → 15 张联系表（`qa-sheets/sheet-00.png` … `sheet-14.png`）
- 额外修复：水龙头抬起 **50° → 35°**（冷水把手挤弯管）
- 其余无错位/重叠/放错

### 预防规则（已写入 Cursor rule + `GSAP_SVG_PITFALLS.md`）

1. from/to 同源，或 SVG 原生 `rotate(a cx cy)`；有 `transform=` 的节点外层套干净 `<g>` 再 tween  
2. 渲前 `qa-scan.py` TOTAL 0 + `npm run check`  
3. 目检要密（0.5s），重点看起止与停顿，不只中点  
4. 不把子任务自查当验收  

## 已知未改（有意保留）

- 成片 ~85s vs BRIEF 目标 75s（步骤细节保留；若要压到 60s：可砍帧 2 数据段 + 精简帧 4 阀门位置说明）
- BGM 非 MiniMax（接口已下线）
