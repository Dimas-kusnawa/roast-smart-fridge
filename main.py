"""Roast the Smart Fridge: One Line, Best Laugh Wins.

Writes one roast line to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output).

Gate: UTF-8 text, 1-160 characters, one line, roasting a smart home gadget
the writer shares a house with.

3 candidates, head-to-head the way the judge would (criteria in order:
gadget roast, funny with a twist at the end, fresh, one line, specific):
- A (114 chars): "My smart fridge waits until 3 a.m. to dump a tray of ice,
  then pings my phone to ask if I enjoyed the sound of it."
  Real behaviour (ice-maker dump), but the laugh is thin and the 3 a.m.
  ice noise is a known complaint, not a fresh angle.
- B (147 chars): "My video doorbell texts me a photo of myself taking the
  bins out in my underwear, captioned 'person detected', like it doesn't
  know who lives here."
  Sharpest laugh: the doorbell shames you with your own photo and acts
  like a stranger. Freshest image of the three, twist lands in the last
  words, and it names the doorbell's real person-detection photo
  notification. Winner.
- C (140 chars): "My smart thermostat learned my routine so well it now
  turns the heating off the minute I sit down, because it knows I won't
  get up to argue."
  Good sting, but the learning-thermostat angle is a known one, and the
  laugh is softer than B's.

Chosen: B.
"""

import os

# Deterministic: no randomness, no network, no clock. The output is always
# exactly this one line, with no trailing newline, so the gate counts 147.
LINE = (
    "My video doorbell texts me a photo of myself taking the bins out "
    "in my underwear, captioned 'person detected', like it doesn't "
    "know who lives here."
)


def main() -> None:
    # Gate self-check: 1-160 chars, one line, UTF-8.
    assert 1 <= len(LINE) <= 160, f"line is {len(LINE)} chars"
    assert "\n" not in LINE, "line must be a single line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
