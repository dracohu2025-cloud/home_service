"""Static QA scan for the transform bugs that slipped into earlier renders.

Flags, per frame file:
  A. origin asymmetry — a fromTo whose from-vars and to-vars disagree on svgOrigin/transformOrigin
     (the pivot jumps under seek; the clock-hand bug).
  B. transform clobbering — a GSAP x/y/scale/rotation tween targeting an SVG element (or its id)
     that also carries its own `transform="..."` attribute (GSAP overwrites it; the drop bug).
  C. transform-attribute groups inside pasted SVG that GSAP rotates without any svgOrigin.
Usage: python3 scripts/qa-scan.py [compositions/frames/*.html]
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
files = [Path(a) for a in sys.argv[1:]] or sorted((ROOT / "compositions" / "frames").glob("*.html"))
XFORM_KEYS = re.compile(r"\b(x|y|scale|scaleX|scaleY|rotation|rotate)\s*:")
ORIGIN = re.compile(r"(svgOrigin|transformOrigin)\s*:\s*\"([^\"]+)\"")


def split_vars(call: str):
    """Return (from_vars, to_vars) text blocks of a tl.fromTo(target, {...}, {...}, t) call."""
    depth, blocks, start = 0, [], None
    for i, ch in enumerate(call):
        if ch == "{":
            if depth == 0:
                start = i
            depth += 1
        elif ch == "}":
            depth -= 1
            if depth == 0 and start is not None:
                blocks.append(call[start : i + 1])
    return (blocks + ["", ""])[:2]


total = 0
for f in files:
    html = f.read_text()
    issues = []
    ids_with_transform = set(re.findall(r'<(?:g|path|rect|circle|ellipse|line|polygon|text|use)\b[^>]*\bid="([^"]+)"[^>]*\btransform="', html))
    ids_with_transform |= set(re.findall(r'<(?:g|path|rect|circle|ellipse|line|polygon|text|use)\b[^>]*\btransform="[^"]*"[^>]*\bid="([^"]+)"', html))
    for m in re.finditer(r"tl\.(fromTo|to|from)\(([^;]*?)\)\s*;", html, flags=re.S):
        kind, body = m.group(1), m.group(2)
        line = html.count("\n", 0, m.start()) + 1
        target = body.split(",")[0].strip()
        fv, tv = split_vars(body) if kind == "fromTo" else (split_vars(body)[0], "")
        vars_all = fv + tv
        if kind == "fromTo" and XFORM_KEYS.search(vars_all):
            of, ot = ORIGIN.findall(fv), ORIGIN.findall(tv)
            if of != ot and (of or ot):
                issues.append(f"L{line} A origin asymmetry {target}: from={of} to={ot}")
        if XFORM_KEYS.search(vars_all):
            for tid in re.findall(r"#([\w-]+)", target):
                if tid in ids_with_transform:
                    issues.append(f"L{line} B GSAP transform on element that has its own transform attr: #{tid}")
            if re.search(r"rotation\s*:", vars_all) and not ORIGIN.search(vars_all):
                for tid in re.findall(r"#([\w-]+)", target):
                    if re.search(rf'<(?:g|path|rect|circle|line)\b[^>]*id="{re.escape(tid)}"', html):
                        issues.append(f"L{line} C SVG rotation without svgOrigin: #{tid}")
    total += len(issues)
    print(f"== {f.name}: {len(issues)} issue(s)")
    for i in issues:
        print("   ", i)
print("TOTAL", total)
