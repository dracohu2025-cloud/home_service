"""Auto-patch GSAP fromTo origin asymmetry (qa-scan flag A).

For each tl.fromTo where from-vars and to-vars disagree on svgOrigin/transformOrigin,
copy the non-empty side onto the empty side, or prefer the to-vars origin if both differ.

Usage:
  python3 scripts/fix-origin-asymmetry.py           # write fixes
  python3 scripts/fix-origin-asymmetry.py --dry-run # report only
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DRY = "--dry-run" in sys.argv
files = [Path(a) for a in sys.argv[1:] if not a.startswith("-")] or sorted(
    (ROOT / "compositions" / "frames").glob("*.html")
)
ORIGIN = re.compile(r"(svgOrigin|transformOrigin)\s*:\s*\"([^\"]+)\"")


def split_var_blocks(call: str) -> list[tuple[int, int, str]]:
    """Return list of (start, end, text) for top-level {...} blocks in a fromTo call body."""
    depth, blocks, start = 0, [], None
    for i, ch in enumerate(call):
        if ch == "{":
            if depth == 0:
                start = i
            depth += 1
        elif ch == "}":
            depth -= 1
            if depth == 0 and start is not None:
                blocks.append((start, i + 1, call[start : i + 1]))
    return blocks


patched = 0
for f in files:
    html = f.read_text()
    out = []
    last = 0
    file_fixes = 0
    for m in re.finditer(r"tl\.fromTo\(([^;]*?)\)\s*;", html, flags=re.S):
        body = m.group(1)
        blocks = split_var_blocks(body)
        if len(blocks) < 2:
            continue
        (fs, fe, fv), (ts, te, tv) = blocks[0], blocks[1]
        of, ot = ORIGIN.findall(fv), ORIGIN.findall(tv)
        if of == ot or not (of or ot):
            continue
        # Prefer to-origin; if to empty, copy from; if both differ, force to's keys onto from.
        prefer = ot or of
        new_fv = fv
        for key, val in prefer:
            if ORIGIN.search(new_fv):
                new_fv = re.sub(
                    rf"{key}\s*:\s*\"[^\"]+\"",
                    f'{key}: "{val}"',
                    new_fv,
                    count=1,
                )
            else:
                # insert after opening brace
                new_fv = new_fv[0] + f'{key}: "{val}", ' + new_fv[1:]
        new_tv = tv
        for key, val in prefer:
            if ORIGIN.search(new_tv):
                new_tv = re.sub(
                    rf"{key}\s*:\s*\"[^\"]+\"",
                    f'{key}: "{val}"',
                    new_tv,
                    count=1,
                )
            else:
                new_tv = new_tv[0] + f'{key}: "{val}", ' + new_tv[1:]
        new_body = body[:fs] + new_fv + body[fe:ts] + new_tv + body[te:]
        # Map body offsets back into full match (group 1 starts after "tl.fromTo(")
        abs_start = m.start(1)
        out.append(html[last:abs_start])
        out.append(new_body)
        last = m.end(1)
        file_fixes += 1
    if file_fixes:
        new_html = "".join(out) + html[last:]
        print(f"{f.name}: {file_fixes} fromTo origin(s) aligned")
        patched += file_fixes
        if not DRY:
            f.write_text(new_html)
    else:
        print(f"{f.name}: ok")
print(("DRY-RUN " if DRY else "") + f"TOTAL patched {patched}")
