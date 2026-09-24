"""Mark every storyboard frame whose src file exists on disk as `status: animated`."""

import re
from pathlib import Path

root = Path(__file__).resolve().parent.parent
sb = root / "STORYBOARD.md"
text = sb.read_text()


text = re.sub(r"(- status: )outline(\n- src: (compositions/frames/[\w-]+\.html))", lambda m: f"{m.group(1)}{'animated' if (root / m.group(3)).exists() else 'outline'}{m.group(2)}", text)
sb.write_text(text)
done = re.findall(r"- status: animated\n- src: compositions/frames/([\w-]+)\.html", text)
print(f"animated: {len(done)}/9", done)
