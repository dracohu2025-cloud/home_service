"""Procedural BGM + SFX for the leaky-house explainer.

Usage: python3 scripts/synth-audio.py frame_starts.json total_seconds
frame_starts.json maps frame_id -> absolute start seconds in the assembled index.
Writes assets/audio/bgm.wav and assets/audio/sfx.wav (mono, 44.1 kHz, 16-bit).
"""

import json
import sys
import wave
from pathlib import Path

import numpy as np
from scipy.signal import butter, lfilter

SR = 44100
ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "assets" / "audio"
rng = np.random.RandomState(20260924)


def t_axis(dur):
    return np.arange(int(dur * SR)) / SR


def env_ad(n, attack=0.005, decay=0.3):
    t = np.arange(n) / SR
    a = np.clip(t / max(attack, 1e-4), 0, 1)
    return a * np.exp(-t / max(decay, 1e-4))


def bandpass(x, lo, hi, order=2):
    b, a = butter(order, [lo / (SR / 2), hi / (SR / 2)], btype="band")
    return lfilter(b, a, x)


def lowpass(x, hi, order=2):
    b, a = butter(order, hi / (SR / 2), btype="low")
    return lfilter(b, a, x)


def midi(n):
    return 440.0 * 2 ** ((n - 69) / 12)


_PLUCKS = {}


def pluck(freq, dur, bright=0.5):
    key = (round(freq, 3), dur, bright)
    if key not in _PLUCKS:
        _PLUCKS[key] = _pluck(freq, dur, bright)
    return _PLUCKS[key]


def _pluck(freq, dur, bright=0.5):
    """Karplus-Strong plucked string (ukulele-ish)."""
    n = int(dur * SR)
    period = max(2, int(SR / freq))
    buf = rng.uniform(-1, 1, period)
    buf = lowpass(buf, 2000 + 6000 * bright) if period > 12 else buf
    out = np.zeros(n)
    decay = 0.996
    for i in range(n):
        v = buf[i % period]
        out[i] = v
        buf[i % period] = decay * 0.5 * (v + buf[(i + 1) % period])
    return out * env_ad(n, 0.002, dur * 0.6)


def bell(freq, dur, amp=1.0):
    t = t_axis(dur)
    partials = [(1, 1.0), (2.76, 0.4), (5.4, 0.18)]
    s = sum(a * np.sin(2 * np.pi * freq * m * t) * np.exp(-t * (2.2 + m)) for m, a in partials)
    return amp * s * env_ad(len(t), 0.002, dur)


def sine_sweep(f0, f1, dur, curve=1.0):
    t = t_axis(dur)
    k = (t / dur) ** curve
    f = f0 + (f1 - f0) * k
    phase = 2 * np.pi * np.cumsum(f) / SR
    return np.sin(phase)


def add(dst, src, at, gain=1.0):
    i = int(at * SR)
    if i >= len(dst):
        return
    j = min(len(dst), i + len(src))
    dst[i:j] += gain * src[: j - i]


# ---------------------------------------------------------------- SFX voices
def sfx_drip():
    s = sine_sweep(1500, 380, 0.14, 0.5) * env_ad(int(0.14 * SR), 0.001, 0.05)
    tail = sine_sweep(700, 900, 0.12) * env_ad(int(0.12 * SR), 0.001, 0.04) * 0.3
    out = np.zeros(int(0.3 * SR))
    add(out, s, 0)
    add(out, tail, 0.06)
    return out


def sfx_boing():
    dur = 0.55
    t = t_axis(dur)
    f = 520 * np.exp(-t * 2.2) + 140 + 40 * np.sin(2 * np.pi * 14 * t) * np.exp(-t * 3)
    s = np.sin(2 * np.pi * np.cumsum(f) / SR)
    return s * env_ad(len(t), 0.003, 0.25)


def sfx_pop():
    return sine_sweep(320, 1100, 0.07, 0.6) * env_ad(int(0.07 * SR), 0.001, 0.03)


def sfx_whoosh(dur=0.45):
    n = int(dur * SR)
    noise = rng.uniform(-1, 1, n)
    x = bandpass(noise, 400, 3500)
    t = np.arange(n) / n
    return x * np.sin(np.pi * t) ** 2 * 0.9


def sfx_clatter():
    out = np.zeros(int(0.7 * SR))
    for k, at in enumerate([0.0, 0.07, 0.15, 0.26, 0.38]):
        f = [2100, 2900, 1700, 3300, 2500][k]
        t = t_axis(0.18)
        s = (np.sin(2 * np.pi * f * t) + 0.6 * np.sin(2 * np.pi * f * 1.47 * t)) * np.exp(-t * 28)
        s += bandpass(rng.uniform(-1, 1, len(t)), 2000, 7000) * np.exp(-t * 60) * 0.6
        add(out, s, at, 0.55 - k * 0.07)
    return out


def sfx_ding():
    out = bell(1318.5, 1.2, 0.8)
    add(out, bell(1975.5, 1.0, 0.35), 0)
    return out


def sfx_ring(dur=1.2):
    t = t_axis(dur)
    tone = np.sin(2 * np.pi * 1180 * t) + 0.7 * np.sin(2 * np.pi * 1420 * t)
    trem = (np.sin(2 * np.pi * 22 * t) > 0).astype(float)
    gate = ((t % 0.6) < 0.45).astype(float)
    return tone * trem * gate * 0.45


def sfx_click():
    t = t_axis(0.04)
    return bandpass(rng.uniform(-1, 1, len(t)), 1500, 6000) * np.exp(-t * 180)


def sfx_tick():
    t = t_axis(0.03)
    return np.sin(2 * np.pi * 2600 * t) * np.exp(-t * 220) * 0.6


def sfx_scribble():
    n = int(0.32 * SR)
    x = bandpass(rng.uniform(-1, 1, n), 1800, 6000)
    t = np.arange(n) / SR
    am = 0.5 + 0.5 * np.sin(2 * np.pi * 28 * t)
    return x * am * np.sin(np.pi * t / 0.32) * 0.7


def sfx_unroll(dur=2.0):
    n = int(dur * SR)
    x = bandpass(rng.uniform(-1, 1, n), 900, 5000)
    t = np.arange(n) / SR
    crackle = (rng.uniform(0, 1, n) > 0.9993).astype(float) * rng.uniform(0.4, 1, n)
    crackle = bandpass(crackle, 1500, 8000) * 6
    return (x * 0.35 + crackle) * np.sin(np.pi * t / dur) ** 0.5


def sfx_stamp():
    t = t_axis(0.4)
    thud = np.sin(2 * np.pi * (95 * np.exp(-t * 6) + 45) * t) * np.exp(-t * 11)
    slap = bandpass(rng.uniform(-1, 1, len(t)), 300, 3000) * np.exp(-t * 45) * 0.7
    return thud + slap


def sfx_hammer():
    t = t_axis(0.2)
    knock = np.sin(2 * np.pi * 180 * t) * np.exp(-t * 35)
    wood = bandpass(rng.uniform(-1, 1, len(t)), 800, 4000) * np.exp(-t * 70) * 0.8
    return knock + wood


def sfx_sparkle():
    out = np.zeros(int(1.0 * SR))
    for k, n in enumerate([84, 88, 91, 96]):
        add(out, bell(midi(n), 0.6, 0.35), k * 0.07)
    return out


def sfx_chime():
    out = np.zeros(int(2.0 * SR))
    for k, n in enumerate([72, 76, 79]):
        add(out, bell(midi(n), 1.8, 0.4), k * 0.05)
    return out


def sfx_whoosh_slam():
    out = np.zeros(int(0.9 * SR))
    add(out, sfx_whoosh(0.35), 0, 0.8)
    add(out, sfx_stamp(), 0.3, 0.9)
    return out


VOICES = {
    "drip": (sfx_drip, 0.55),
    "boing": (sfx_boing, 0.45),
    "pop": (sfx_pop, 0.35),
    "whoosh": (sfx_whoosh, 0.25),
    "clatter": (sfx_clatter, 0.5),
    "ding": (sfx_ding, 0.3),
    "ring": (sfx_ring, 0.22),
    "click": (sfx_click, 0.4),
    "tick": (sfx_tick, 0.25),
    "scribble": (sfx_scribble, 0.3),
    "unroll": (sfx_unroll, 0.3),
    "stamp": (sfx_stamp, 0.6),
    "hammer": (sfx_hammer, 0.55),
    "sparkle": (sfx_sparkle, 0.35),
    "chime": (sfx_chime, 0.3),
    "slam": (sfx_whoosh_slam, 0.5),
}

CUES = [
    ("01-hook-leak", [(1.3, "drip"), (2.0, "drip"), (2.7, "drip"), (3.1, "boing")]),
    ("02-stakes-cost", [(0.4, "drip"), (1.1, "drip"), (1.5, "whoosh"), (3.6, "ding")]),
    ("03-step1-diy", [(0.3, "whoosh"), (2.3, "clatter"), (3.0, "boing"), (4.4, "pop"), (5.6, "pop")]),
    ("04-step2-neighbor", [(1.6, "pop"), (2.0, "pop"), (3.3, "whoosh"), (4.8, "ding"), (5.8, "pop")]),
    ("05-step3-phone", [(0.4, "ring"), (1.7, "click")]
     + [(2.0 + 0.2 * k, "tick") for k in range(8)]
     + [(4.0, "scribble"), (4.5, "scribble"), (5.0, "scribble")]),
    ("06-step4-quote", [(1.4, "unroll"), (2.2, "pop"), (2.6, "pop"), (3.0, "pop"), (3.9, "boing"), (5.4, "stamp")]),
    ("07-step5-choose", [(1.4, "whoosh"), (1.7, "whoosh"), (2.0, "whoosh"), (3.6, "ding"),
                         (5.2, "pop"), (5.8, "pop"), (6.4, "pop"), (7.0, "pop")]),
    ("08-fixed-sunrise", [(1.2, "hammer"), (1.6, "hammer"), (2.0, "hammer"), (3.4, "sparkle"), (4.2, "chime")]),
    ("09-thesis-trust", [(0.4, "pop"), (0.8, "pop"), (1.2, "pop"), (1.6, "pop"), (2.0, "pop"),
                         (2.75, "slam"), (5.6, "chime")]),
]


# ---------------------------------------------------------------- BGM
def build_bgm(total, starts):
    out = np.zeros(int((total + 1) * SR))
    bpm = 108
    beat = 60 / bpm
    bar = 4 * beat
    # C  Am  F  G  (ukulele voicings, MIDI)
    chords = [[60, 64, 67, 72], [57, 60, 64, 69], [53, 57, 60, 65], [55, 59, 62, 67]]
    bass = [36, 33, 29, 31]
    melody = [
        [(0, 76), (1, 79), (2.5, 77), (3, 76)],
        [(0, 72), (1.5, 74), (2, 76)],
        [(0, 77), (1, 76), (2, 74), (3, 72)],
        [(0, 74), (2, 79)],
    ]
    intro_end = starts.get("02-stakes-cost", 5.0)
    sunrise = starts.get("08-fixed-sunrise", 46.0)
    strum_pattern = [0, 1, 1.5, 2.5, 3]
    n_bars = int(np.ceil(total / bar))
    for b in range(n_bars):
        t0 = b * bar
        ci = b % 4
        night = t0 < intro_end
        lift = t0 >= sunrise
        for k, off in enumerate(strum_pattern):
            at = t0 + off * beat
            if at >= total:
                continue
            if night and k not in (0, 3):
                continue
            g = 0.16 if k == 0 else 0.1
            for s, note in enumerate(chords[ci]):
                add(out, pluck(midi(note), 0.9, 0.35 if night else 0.55), at + s * 0.012, g)
        if not night:
            bt = t_axis(bar * 0.95)
            f = midi(bass[ci])
            bs = np.sin(2 * np.pi * f * bt) + 0.3 * np.sin(2 * np.pi * 2 * f * bt)
            for half in (0, 2):
                add(out, bs[: int(beat * 1.8 * SR)] * env_ad(int(beat * 1.8 * SR), 0.01, 0.5), t0 + half * beat, 0.16)
            for q in range(8):
                nz = bandpass(rng.uniform(-1, 1, int(0.06 * SR)), 5000, 11000) * env_ad(int(0.06 * SR), 0.002, 0.02)
                add(out, nz, t0 + q * beat / 2, 0.05 if q % 2 else 0.03)
        mel_gain = 0.12 if lift else 0.08
        for off, note in melody[ci]:
            at = t0 + off * beat
            if at < total:
                add(out, bell(midi(note), 0.9, 1.0), at, mel_gain)
    out = out[: int(total * SR)]
    fade_in = int(0.8 * SR)
    fade_out = int(1.8 * SR)
    out[:fade_in] *= np.linspace(0, 1, fade_in)
    out[-fade_out:] *= np.linspace(1, 0, fade_out)
    return out


def write_wav(path, x, peak=0.89):
    m = np.max(np.abs(x)) or 1
    y = (x / m * peak * 32767).astype(np.int16)
    path.parent.mkdir(parents=True, exist_ok=True)
    with wave.open(str(path), "wb") as w:
        w.setnchannels(1)
        w.setsampwidth(2)
        w.setframerate(SR)
        w.writeframes(y.tobytes())


def main():
    starts = json.loads(Path(sys.argv[1]).read_text())
    total = float(sys.argv[2])
    sfx = np.zeros(int((total + 1) * SR))
    for frame_id, cues in CUES:
        if frame_id not in starts:
            print("missing start for", frame_id)
            continue
        for off, kind in cues:
            fn, gain = VOICES[kind]
            add(sfx, fn(), starts[frame_id] + off, gain)
    write_wav(OUT / "sfx.wav", sfx[: int(total * SR)], peak=0.9)
    write_wav(OUT / "bgm.wav", build_bgm(total, starts), peak=0.8)
    print("wrote", OUT / "bgm.wav", "and", OUT / "sfx.wav")


if __name__ == "__main__":
    main()
