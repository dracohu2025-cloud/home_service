"""Mount the procedural BGM + SFX tracks into index.html (idempotent; rerun after assemble)."""

import re
from pathlib import Path

root = Path(__file__).resolve().parent.parent
index = root / "index.html"
html = index.read_text()
html = re.sub(r"\n      <!-- procedural-audio -->.*?<!-- /procedural-audio -->", "", html, flags=re.S)

total = re.search(r'id="root"[^>]*?data-duration="([\d.]+)"', html, flags=re.S).group(1)
block = f"""
      <!-- procedural-audio -->
      <audio id="el-bgm" src="assets/audio/bgm.wav" data-start="0" data-duration="{total}" data-track-index="11" data-volume="0.55"></audio>
      <audio id="el-sfx" src="assets/audio/sfx.wav" data-start="0" data-duration="{total}" data-track-index="20" data-volume="0.9"></audio>
      <!-- /procedural-audio -->"""

last_frame = list(re.finditer(r'<div\s+id="el-09-thesis-trust".*?></div>', html, flags=re.S))[-1]
html = html[: last_frame.end()] + block + html[last_frame.end():]
index.write_text(html)
print("mounted bgm + sfx, duration", total)
