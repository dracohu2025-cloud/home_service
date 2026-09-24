"""Synthesize refined SFX from each STORYBOARD frame's `sfx:` cue line and register them in audio_meta.json.

Cue grammar (per frame): "<name> at 0.7s" · "<name> at 1.72, 1.9, 2.1s" · "<name> 2.3–3.4s" (range = duration).
Writes assets/sfx/<name>.wav (one file per sound kind, fixed length) and audio_meta.sfx[].
"""

import json
import re
import wave
from pathlib import Path

import numpy as np
from scipy.signal import butter, lfilter

SR = 44100
ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "assets" / "sfx"
rng = np.random.RandomState(7)


def t(d):
    return np.arange(int(d * SR)) / SR


def env(n, a=0.004, d=0.2):
    x = np.arange(n) / SR
    return np.clip(x / a, 0, 1) * np.exp(-x / d)


def bp(x, lo, hi):
    b, a = butter(2, [lo / (SR / 2), hi / (SR / 2)], btype="band")
    return lfilter(b, a, x)


def lp(x, hi):
    b, a = butter(2, hi / (SR / 2), btype="low")
    return lfilter(b, a, x)


def noise(d):
    return rng.uniform(-1, 1, int(d * SR))


def sweep(f0, f1, d, curve=1.0):
    k = (t(d) / d) ** curve
    return np.sin(2 * np.pi * np.cumsum(f0 + (f1 - f0) * k) / SR)


def bell(f, d, decay=3.0):
    x = t(d)
    return (np.sin(2 * np.pi * f * x) + 0.35 * np.sin(2 * np.pi * f * 2.01 * x) + 0.12 * np.sin(2 * np.pi * f * 3.02 * x)) * np.exp(-x * decay)


def whoosh(d=0.42, lo=500, hi=4200):
    n = noise(d)
    x = bp(n, lo, hi)
    s = np.linspace(0, 1, len(x))
    return x * np.sin(np.pi * s) ** 1.6 * 0.9


def mix(*parts):
    L = max(int(at * SR) + len(p) for at, p in parts)
    out = np.zeros(L + int(0.01 * SR))
    for at, p in parts:
        i = int(at * SR)
        out[i : i + len(p)] += p[: len(out) - i]
    return out


SOUNDS = {
    "tick": lambda d: np.sin(2 * np.pi * 3200 * t(0.035)) * np.exp(-t(0.035) * 180) * 0.8,
    "tick-run": lambda d: mix(*[(k * 0.09, np.sin(2 * np.pi * 2800 * t(0.03)) * np.exp(-t(0.03) * 200) * 0.6) for k in range(max(2, int(d / 0.09)))]),
    "hiss": lambda d: bp(noise(d), 3000, 9000) * np.minimum(1, t(d) / 0.3) * np.minimum(1, (d - t(d)) / 0.2) * 0.6,
    "spray-burst": lambda d: mix((0, sweep(180, 60, 0.18) * env(int(0.18 * SR), 0.002, 0.08)), (0.02, bp(noise(1.2), 1500, 8000) * env(int(1.2 * SR), 0.01, 0.5) * 0.7)),
    "whoosh": lambda d: whoosh(0.4),
    "card-whoosh": lambda d: whoosh(0.3, 800, 5000) * 0.8,
    "chime": lambda d: mix((0, bell(1046.5, 1.6)), (0.06, bell(1568, 1.4) * 0.6), (0.12, bell(2093, 1.2) * 0.35)) * 0.6,
    "pop": lambda d: sweep(420, 1300, 0.06, 0.5) * env(int(0.06 * SR), 0.001, 0.025) * 0.8,
    "valve-turn": lambda d: bp(noise(d), 200, 1400) * (0.55 + 0.45 * np.sin(2 * np.pi * 9 * t(d))) * np.minimum(1, t(d) / 0.08) * np.minimum(1, (d - t(d)) / 0.1) * 0.55,
    "click": lambda d: bp(noise(0.03), 1500, 7000) * np.exp(-t(0.03) * 220),
    "breaker-click": lambda d: mix((0, bp(noise(0.04), 800, 6000) * np.exp(-t(0.04) * 160)), (0.0, sweep(160, 90, 0.08) * env(int(0.08 * SR), 0.001, 0.03) * 0.8)),
    "warn-tone": lambda d: mix((0, np.sin(2 * np.pi * 660 * t(0.16)) * env(int(0.16 * SR), 0.005, 0.1)), (0.17, np.sin(2 * np.pi * 520 * t(0.2)) * env(int(0.2 * SR), 0.005, 0.12))) * 0.5,
    "water-run": lambda d: lp(bp(noise(d), 300, 6000), 5000) * (0.8 + 0.2 * np.sin(2 * np.pi * 5 * t(d))) * np.minimum(1, t(d) / 0.15) * np.minimum(1, (d - t(d)) / 0.3) * 0.5,
    "flush": lambda d: bp(noise(d), 200, 3500) * np.sin(np.pi * t(d) / d) ** 0.7 * 0.6,
    "fizz": lambda d: bp(noise(0.5), 2500, 9000) * np.exp(-t(0.5) * 6) * 0.5,
    "shutter": lambda d: mix((0, bp(noise(0.03), 2000, 9000) * np.exp(-t(0.03) * 200)), (0.06, bp(noise(0.04), 1200, 7000) * np.exp(-t(0.04) * 150) * 0.8)),
    "rec-beep": lambda d: np.sin(2 * np.pi * 1760 * t(0.09)) * env(int(0.09 * SR), 0.003, 0.05) * 0.5,
    "buzz": lambda d: np.sign(np.sin(2 * np.pi * 130 * t(0.28))) * env(int(0.28 * SR), 0.005, 0.16) * 0.25,
    "swing": lambda d: whoosh(0.5, 300, 2500) * 0.7,
}


def parse_cues(sb: str):
    cues = []
    frame = None
    for line in sb.splitlines():
        h = re.match(r"^## Frame (\d+)", line)
        if h:
            frame = int(h.group(1))
        m = re.match(r"^- sfx:\s*(.+)$", line)
        if not (m and frame):
            continue
        for part in m.group(1).split(";"):
            part = part.strip().replace("–", "-")
            r = re.match(r"^([\w-]+)\s+([\d.]+)-([\d.]+)s$", part)
            if r:
                a, b = float(r.group(2)), float(r.group(3))
                cues.append((frame, r.group(1), a, b - a))
                continue
            p = re.match(r"^([\w-]+)\s+at\s+(.+?)s$", part)
            if p:
                for tt in p.group(2).split(","):
                    cues.append((frame, p.group(1), float(tt.strip().rstrip("s")), None))
                continue
            print("unparsed sfx cue:", frame, part)
    return cues


def write_wav(path, x, peak=0.8):
    m = np.max(np.abs(x)) or 1
    y = (x / m * peak * 32767).astype(np.int16)
    with wave.open(str(path), "wb") as w:
        w.setnchannels(1)
        w.setsampwidth(2)
        w.setframerate(SR)
        w.writeframes(y.tobytes())


VOLUME = {"hiss": 0.22, "water-run": 0.2, "flush": 0.22, "tick-run": 0.18, "whoosh": 0.22, "card-whoosh": 0.2,
          "chime": 0.26, "pop": 0.2, "spray-burst": 0.32, "valve-turn": 0.26, "warn-tone": 0.22, "buzz": 0.2}


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    cues = parse_cues((ROOT / "STORYBOARD.md").read_text())
    entries = []
    for frame, name, at, dur in cues:
        if name not in SOUNDS:
            print("unknown sfx:", name)
            continue
        key = f"{name}-{dur:.2f}" if dur else name
        path = OUT / f"{key}.wav"
        if not path.exists():
            write_wav(path, SOUNDS[name](dur or 0.5), 0.85)
        length = wave.open(str(path)).getnframes() / SR
        entries.append({"frame": frame, "file": f"assets/sfx/{path.name}", "offset_s": round(at, 3),
                        "duration_s": round(length, 3), "volume": VOLUME.get(name, 0.25)})
    meta_path = ROOT / "audio_meta.json"
    meta = json.loads(meta_path.read_text())
    meta["sfx"] = entries
    meta["bgm"] = {"path": "assets/bgm/bgm-elevenlabs.mp3", "volume": 0.13}
    meta_path.write_text(json.dumps(meta, indent=2))
    print(f"{len(entries)} sfx cues →", meta_path)


if __name__ == "__main__":
    main()
