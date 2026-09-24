"""Generate the upbeat instrumental bed on fal.ai (MiniMax music API is retired for this account).

Reads FAL_API_KEY / FAL_KEY from the environment.
Usage: python3 scripts/make-bgm-fal.py <model> <seconds> [out.mp3]
  model: elevenlabs | stable-audio
"""

import json
import os
import sys
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PROMPT = (
    "Upbeat, bright, polished modern explainer background music at 120 BPM. Plucky marimba and "
    "muted electric guitar hook, handclaps and finger snaps, light funky bass, crisp tight drums, "
    "airy synth pad. Playful, confident, curious, optimistic. Full groove from the very first second, "
    "no intro, no fade-in, steady energy throughout, clean premium mix that sits under a spoken voiceover. "
    "Instrumental only, no vocals."
)
MODELS = {
    "elevenlabs": ("fal-ai/elevenlabs/music", lambda s: {"prompt": PROMPT, "music_length_ms": int(s * 1000), "force_instrumental": True}),
    "stable-audio": ("fal-ai/stable-audio-25/text-to-audio", lambda s: {"prompt": PROMPT, "seconds_total": int(s)}),
}


def find_url(obj):
    if isinstance(obj, dict):
        for k in ("audio", "audio_file", "file"):
            v = obj.get(k)
            if isinstance(v, dict) and v.get("url"):
                return v["url"]
            if isinstance(v, str) and v.startswith("http"):
                return v
        for v in obj.values():
            u = find_url(v)
            if u:
                return u
    if isinstance(obj, list):
        for v in obj:
            u = find_url(v)
            if u:
                return u
    return None


def main():
    model_key, seconds = sys.argv[1], float(sys.argv[2])
    dest = Path(sys.argv[3]) if len(sys.argv) > 3 else ROOT / "assets" / "bgm" / f"bgm-{model_key}.mp3"
    key = (os.environ.get("FAL_API_KEY") or os.environ.get("FAL_KEY") or "").strip()
    model, build = MODELS[model_key]
    req = urllib.request.Request(
        f"https://fal.run/{model}",
        data=json.dumps(build(seconds)).encode(),
        headers={"Authorization": f"Key {key}", "Content-Type": "application/json"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=900) as r:
            result = json.loads(r.read().decode())
    except urllib.error.HTTPError as e:
        raise SystemExit(f"{model} HTTP {e.code}: {e.read().decode()[:400]}")
    url = find_url(result)
    if not url:
        raise SystemExit("no audio url in response: " + json.dumps(result)[:400])
    dest.parent.mkdir(parents=True, exist_ok=True)
    with urllib.request.urlopen(url, timeout=300) as r:
        dest.write_bytes(r.read())
    print("wrote", dest, dest.stat().st_size, "bytes")


if __name__ == "__main__":
    main()
