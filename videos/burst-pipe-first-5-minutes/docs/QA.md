# Visual QA — Pipe Burst first 5 minutes

## Findings (shipped once, then fixed)

| # | Symptom | Root cause | Fix |
|---|---|---|---|
| 1 | Clock hands wrong in final video | GSAP `fromTo` with mismatched `svgOrigin` / `transformOrigin` (pivot jumps on seek) | Prefer SVG `rotate(a cx cy)`; make from/to origins identical. Patched **18** asymmetries → 0 |
| 2 | “Blue drip” segment unreadable | Abstract drip + GSAP `x/y/rotation` clobbering SVG `transform=` | Redrew pipe + crack + drops; animate outer `<g>` without attribute transform |
| 3 | Faucet angle too extreme | Design choice | 50° → 35° |
| 4 | Font lint | Fredoka One | Space Grotesk + Inter only |

Full technical rules: [`../../docs/GSAP_SVG_PITFALLS.md`](../../docs/GSAP_SVG_PITFALLS.md).

## Prevention gate (run before every render)

```bash
python3 scripts/qa-scan.py
# must report zero A/B/C issues
```

## Dense review method

1. Extract a frame every **0.5s** from the final MP4 (original run: ~184 PNGs under `/tmp/pipe-test/qa/`).
2. Montage into contact sheets (10–12 thumbs per sheet).
3. Review for empty beats, overlap, broken pivots, caption collisions, illegible icons.

### Archived contact sheets (this commit)

`docs/qa-sheets/sheet-00.png` … `sheet-14.png` — full pass over the post-fix master. Use these to see what “good” looked like after clock + drip fixes.

Mid-point snapshots used during production may also live under project `renders/` or asset folders from earlier commits.

## Checklist for future edits

- [ ] `qa-scan.py` clean
- [ ] No GSAP transform props on nodes with `transform=`
- [ ] Matching svgOrigin in every fromTo
- [ ] Spot-check new dense sheets after re-encode
- [ ] Caption vs VO spot-listen (esp. numbers and “2 a.m.”)
- [ ] BGM still from fal path (not MiniMax music-3.0-free)
