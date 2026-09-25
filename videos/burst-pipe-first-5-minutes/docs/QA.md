# Visual QA — Pipe Burst first 5 minutes

完整修复叙事见 [`CHANGELOG.md`](CHANGELOG.md)。技术硬规则见 [`../../docs/GSAP_SVG_PITFALLS.md`](../../docs/GSAP_SVG_PITFALLS.md)。

## 用户指出的问题

1. **时钟指针错位** — `feedback/01-clock-hands-misaligned.png`  
   根因：`svgOrigin` 只在 to-vars。  
2. **蓝线语义不清** — `feedback/02-abstract-drip-incomprehensible.png`  
   根因：抽象滴水缩略不可读（非单纯放错位）。

## 自查追加

| # | 发现 | 修复 |
|---|---|---|
| 17 | origin 不对称（同时钟类），帧 1/2/4/5/9 | from/to 同源 |
| 1 | 马桶漩涡无旋转原点 | 固定圆心 |
| 1 | 水龙头 50° 挤弯管 | → 35° |

`qa-scan.py`：18 → **0**。

## 预防门禁（渲染前必过）

```bash
python3 scripts/qa-scan.py   # TOTAL must be 0
npm run check
```

目检：每 0.5s 截帧拼联系表（归档：`qa-sheets/`）。不要只抽场景中点；不要把子任务自查当验收。

## Checklist

- [ ] `qa-scan.py` clean  
- [ ] 无 GSAP transform 打在带 `transform=` 的节点上  
- [ ] fromTo 同源  
- [ ] 重渲后扫联系表或至少抽起止帧  
- [ ] 字幕 vs VO（数字、「2 a.m.」）  
- [ ] BGM 走 `make-bgm-fal.py`  
