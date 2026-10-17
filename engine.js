// Jigsaw Math engine - pieces, borders, and minutes, run exactly.
// Mirrored float-for-float by oracle.py; keep the op order identical.

function _pos(x, msg) {
  if (!isFinite(x) || x <= 0) throw new Error(msg);
  return x;
}

function _comma(n) {
  var s = String(n), out = "";
  while (s.length > 3) { out = "," + s.slice(-3) + out; s = s.slice(0, -3); }
  return s + out;
}

// floor(x*10+0.5)/10 matches Python identically for positive x.
function _round1(x) {
  return Math.floor(x * 10 + 0.5) / 10;
}

function _fmt1(x) {
  return x % 1 === 0 ? String(x) : x.toFixed(1);
}

// The grid truth: what the piece count really cuts into.
function gridTruth(pieces) {
  _pos(pieces, "count at least 1 piece");
  if (pieces !== Math.floor(pieces)) throw new Error("pieces come whole");
  var w = pieces, h = 1;
  for (var f = Math.floor(Math.sqrt(pieces)); f >= 2; f--) {
    if (pieces % f === 0) { h = f; w = pieces / f; break; }
  }
  if (h === 1) {
    return _comma(pieces) + " is prime - no grid cuts evenly, so the box is making it up.";
  }
  return _comma(pieces) + " pieces cut " + w + " by " + h + ".";
}

// The border truth: the easy first hour, measured.
function borderTruth(w, h) {
  if (!isFinite(w) || w < 2 || !isFinite(h) || h < 2) throw new Error("a grid needs at least 2 by 2");
  if (w !== Math.floor(w) || h !== Math.floor(h)) throw new Error("pieces come whole");
  var border = 2 * w + 2 * h - 4;
  var total = w * h;
  var middle = total - border;
  var pct = _round1(border * 100 / total);
  return _comma(border) + " border piece" + (border === 1 ? "" : "s") + ", " + _comma(middle) +
    " middle - the border is " + _fmt1(pct) + "% of the puzzle.";
}

// The time truth: the evening, itemized.
function timeTruth(pieces, perMinute) {
  _pos(pieces, "count at least 1 piece");
  _pos(perMinute, "pieces a minute must be more than 0");
  var minutes = Math.floor(pieces / perMinute + 0.5);
  var head = _comma(pieces) + " pieces at " + _fmt1(perMinute) + " a minute is " + _comma(minutes) + " minute" + (minutes === 1 ? "" : "s");
  var hours = Math.floor(minutes / 60), mins = minutes % 60;
  if (hours === 0) return head + ".";
  var span;
  if (mins === 0) span = hours + " hour" + (hours === 1 ? "" : "s");
  else span = hours + " hour" + (hours === 1 ? "" : "s") + " " + mins + " minute" + (mins === 1 ? "" : "s");
  return head + " - " + span + ".";
}
