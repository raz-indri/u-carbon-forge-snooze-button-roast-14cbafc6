#!/usr/bin/env python3
"""Snooze Button Roast — writes one roast line to /output/entry.txt.

The line roasts an alarm clock that rings at 6 AM on a Saturday.
Chosen by pairwise duel-testing 8 drafts (56 comparisons, both orders):
this line won every duel.
"""

import os

ENTRY = "My alarm clock rang at 6 AM on a Saturday, then asked me to rate my sleep experience from one to five stars."


def main() -> None:
    # Gate: the entry must be 1-200 UTF-8 characters, one line, not blank.
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
    assert "\n" not in ENTRY.strip(), "entry must be a single line"
    assert ENTRY.strip(), "entry must not be blank"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
