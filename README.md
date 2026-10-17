# Jigsaw Math

Jigsaw puzzle honesty. The box says "an evening"; the box has never met your dining table. Jigsaw Math runs the counting exactly: the grid, the border, the minutes.

## What it computes

- **The grid truth** - what the piece count cuts into: 1,000 pieces cut 40 by 25. Prime counts get the truth too: no grid cuts evenly, so the box is making it up.
- **The border truth** - border pieces against the middle: 126 border pieces, 874 middle - the border is 12.6% of the puzzle.
- **The time truth** - the evening, itemized: 1,000 pieces at 4 a minute is 250 minutes - 4 hours 10 minutes.

## Boundary

Counting arithmetic only. Jigsaw Math never judges whether starting the 3,000-piece sky at 9 PM was a good idea.

## Files

- `index.html` - landing page with the honesty pitch and the boundary.
- `app.html` - the interactive calculator.
- `engine.js` - the arithmetic, shared by the app and the tests.
- `oracle.py` - the Python mirror that generates `expected.json`.
- `test.js` - compares every engine output against `expected.json` (14 cases).
- `expected.json` - the golden answers.

## Test

```
python3 oracle.py
node test.js
```

Live: https://ilanis-agent.github.io/jigsawmath/
Repo: https://github.com/iLanis-agent/jigsawmath
