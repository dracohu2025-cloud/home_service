"""Synthesize one MiniMax TTS file per SCRIPT.md frame, then word-time it and write audio_meta.json.

Usage: python3 scripts/make-voice.py [--voice English_expressive_narrator] [--speed 1.06]
"""

import argparse
import difflib
import json
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TRANSCRIBE = Path.home() / ".agents/skills/media-use/scripts/transcribe.mjs"


def parse_script(md: str):
    frames, cur = [], None
    for line in md.splitlines():
        h = re.match(r"^#{2,3}\s+.*?\(frame\s+(\d+)\)", line, re.I)
        if h:
            cur = {"frame": int(h.group(1)), "text": ""}
            frames.append(cur)
            continue
        m = re.match(r"^(?: {4,}|\t)(.+)$", line)
        if cur and m:
            cur["text"] = (cur["text"] + " " + m.group(1).strip()).strip()
    return frames


def norm(token: str) -> str:
    return re.sub(r"[^a-z0-9]", "", token.lower())


def align(script_text: str, heard: list) -> list:
    """Give each script word a time: exact-text matches take the ASR timing, the rest interpolate."""
    tokens = script_text.split()
    times = [None] * len(tokens)
    sm = difflib.SequenceMatcher(a=[norm(t) for t in tokens], b=[norm(w["text"]) for w in heard], autojunk=False)
    for block in sm.get_matching_blocks():
        for k in range(block.size):
            w = heard[block.b + k]
            times[block.a + k] = (w["start"], w["end"])
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag == "replace" and j2 > j1:
            s, e = heard[j1]["start"], heard[j2 - 1]["end"]
            span = (e - s) / (i2 - i1)
            for k in range(i1, i2):
                times[k] = (s + span * (k - i1), s + span * (k - i1 + 1))
    end_all = heard[-1]["end"] if heard else 0.0
    for k, t in enumerate(times):
        if t is None:
            prev_end = next((times[j][1] for j in range(k - 1, -1, -1) if times[j]), 0.0)
            next_start = next((times[j][0] for j in range(k + 1, len(times)) if times[j]), end_all)
            times[k] = (prev_end, max(prev_end + 0.05, next_start))
    return [{"text": t, "start": round(s, 3), "end": round(e, 3)} for t, (s, e) in zip(tokens, times)]


def duration(path: Path) -> float:
    out = subprocess.check_output(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(path)]
    )
    return float(out.decode().strip())


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--voice", default="English_expressive_narrator")
    ap.add_argument("--speed", default="1.06")
    ap.add_argument("--force", action="store_true")
    args = ap.parse_args()

    out_dir = ROOT / "assets" / "voice"
    out_dir.mkdir(parents=True, exist_ok=True)
    voices = []
    for f in parse_script((ROOT / "SCRIPT.md").read_text()):
        n = f"{f['frame']:02d}"
        mp3 = out_dir / f"{n}.mp3"
        if args.force or not mp3.exists():
            subprocess.run(
                ["mmx", "speech", "synthesize", "--text", f["text"], "--voice", args.voice,
                 "--model", "speech-2.8-hd", "--speed", args.speed, "--language", "English",
                 "--sample-rate", "44100", "--bitrate", "128000", "--out", str(mp3),
                 "--quiet", "--non-interactive"],
                check=True,
            )
        words_json = out_dir / f"{n}.words.json"
        if args.force or not words_json.exists():
            subprocess.run(["node", str(TRANSCRIBE), "--input", str(mp3), "--out", str(words_json)], check=True)
        raw = json.loads(words_json.read_text())
        heard = raw.get("words", []) if isinstance(raw, dict) else raw
        voices.append({
            "frame": f["frame"],
            "path": f"assets/voice/{n}.mp3",
            "duration_s": round(duration(mp3), 3),
            "words": align(f["text"], heard),
        })
        print(n, voices[-1]["duration_s"], "s,", len(voices[-1]["words"]), "words")

    meta_path = ROOT / "audio_meta.json"
    meta = json.loads(meta_path.read_text()) if meta_path.exists() else {}
    meta["voices"] = voices
    meta.setdefault("bgm", None)
    meta.setdefault("sfx", [])
    meta_path.write_text(json.dumps(meta, indent=2))
    print("wrote", meta_path)


if __name__ == "__main__":
    main()
