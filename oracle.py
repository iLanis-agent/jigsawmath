#!/usr/bin/env python3
# Jigsaw Math oracle - mirrors engine.js float-for-float.
import json, math

def _pos(x, msg):
    if not math.isfinite(x) or x <= 0:
        raise ValueError(msg)
    return x

def _comma(n):
    return f"{n:,}"

def _round1(x):
    return math.floor(x * 10 + 0.5) / 10

def _fmt1(x):
    return str(int(x)) if x % 1 == 0 else f"{x:.1f}"

def grid_truth(pieces):
    _pos(pieces, "count at least 1 piece")
    if pieces != math.floor(pieces):
        raise ValueError("pieces come whole")
    pieces = int(pieces)
    w, h = pieces, 1
    for f in range(int(math.isqrt(pieces)), 1, -1):
        if pieces % f == 0:
            h, w = f, pieces // f
            break
    if h == 1:
        return f"{_comma(pieces)} is prime - no grid cuts evenly, so the box is making it up."
    return f"{_comma(pieces)} pieces cut {w} by {h}."

def border_truth(w, h):
    if not math.isfinite(w) or w < 2 or not math.isfinite(h) or h < 2:
        raise ValueError("a grid needs at least 2 by 2")
    if w != math.floor(w) or h != math.floor(h):
        raise ValueError("pieces come whole")
    w, h = int(w), int(h)
    border = 2 * w + 2 * h - 4
    total = w * h
    middle = total - border
    pct = _round1(border * 100 / total)
    return (f"{_comma(border)} border piece" + ("" if border == 1 else "s") +
            f", {_comma(middle)} middle - the border is {_fmt1(pct)}% of the puzzle.")

def time_truth(pieces, per_minute):
    _pos(pieces, "count at least 1 piece")
    _pos(per_minute, "pieces a minute must be more than 0")
    minutes = math.floor(pieces / per_minute + 0.5)
    head = (f"{_comma(pieces)} pieces at {_fmt1(per_minute)} a minute is "
            f"{_comma(minutes)} minute" + ("" if minutes == 1 else "s"))
    hours, mins = divmod(minutes, 60)
    if hours == 0:
        return head + "."
    if mins == 0:
        span = f"{hours} hour" + ("" if hours == 1 else "s")
    else:
        span = (f"{hours} hour" + ("" if hours == 1 else "s") +
                f" {mins} minute" + ("" if mins == 1 else "s"))
    return head + f" - {span}."

CASES = [
    ("gridTruth", (1000,)),
    ("gridTruth", (500,)),
    ("gridTruth", (509,)),
    ("gridTruth", (513,)),
    ("gridTruth", (0,)),
    ("gridTruth", (999.5,)),
    ("borderTruth", (40, 25)),
    ("borderTruth", (2, 2)),
    ("borderTruth", (1, 5)),
    ("timeTruth", (1000, 4)),
    ("timeTruth", (90, 2)),
    ("timeTruth", (120, 2)),
    ("timeTruth", (300, 1.5)),
    ("timeTruth", (1000, 0)),
]

FNS = {"gridTruth": grid_truth, "borderTruth": border_truth, "timeTruth": time_truth}

out = []
for name, args in CASES:
    try:
        expected = FNS[name](*args)
    except ValueError as e:
        expected = "ERR:" + str(e)
    out.append({"fn": name, "args": list(args), "expected": expected})

with open("expected.json", "w") as f:
    f.write(json.dumps(out, indent=2) + "\n")
print(f"{len(out)} cases written")
