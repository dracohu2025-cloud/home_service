"""DEPRECATED — MiniMax music-3.0-free returns HTTP 410 Gone.

Use scripts/make-bgm-fal.py (fal ElevenLabs Music + FAL_API_KEY) instead.
This file is kept only as a historical reference of the original prompt/API shape.

Reads MINIMAX_API_KEY from the environment, else from ~/.mmx/config.json.
Usage: python3 scripts/make-bgm.py [out.mp3]  # will fail until MiniMax restores music
"""

import json
import os
import sys
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
API_URL = "https://api.minimaxi.com/v1/music_generation"
PROMPT = (
    "Immediate full groove from the first second, no fade-in, no silent intro. "
    "Upbeat, bright, polished modern explainer background music at 120 BPM. "
    "Plucky marimba and muted electric guitar hook, handclaps and finger snaps, "
    "light funky bass, crisp tight drums, airy synth pad. Playful, confident, curious, optimistic. "
    "Clean premium mix that sits under a spoken voiceover. Instrumental only, no vocals, no humming."
)


def load_key() -> str:
    key = os.environ.get("MINIMAX_API_KEY", "").strip()
    if key:
        return key
    cfg = json.loads((Path.home() / ".mmx" / "config.json").read_text())
    return str(cfg.get("api_key") or "").strip()


def main():
    dest = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "assets" / "bgm" / "bgm-upbeat.mp3"
    payload = {
        "model": "music-3.0-free",
        "prompt": PROMPT,
        "is_instrumental": True,
        "audio_setting": {"sample_rate": 44100, "bitrate": 256000, "format": "mp3"},
        "output_format": "url",
    }
    req = urllib.request.Request(
        API_URL,
        data=json.dumps(payload).encode(),
        headers={"Authorization": f"Bearer {load_key()}", "Content-Type": "application/json"},
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=600) as r:
        result = json.loads(r.read().decode())
    data = result.get("data") if isinstance(result.get("data"), dict) else {}
    url = result.get("audio") or data.get("audio") or data.get("audio_url")
    if not url:
        raise SystemExit("music generation failed: " + json.dumps(result)[:400])
    dest.parent.mkdir(parents=True, exist_ok=True)
    with urllib.request.urlopen(url, timeout=300) as r:
        dest.write_bytes(r.read())
    print("wrote", dest, dest.stat().st_size, "bytes")


if __name__ == "__main__":
    main()
