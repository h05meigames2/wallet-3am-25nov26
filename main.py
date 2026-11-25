#!/usr/bin/env python3
"""The 3 AM Excuse — entry for make.fun bounty
u-hazel-walrus-38-4764-the-3-am-excuse-c1017878.

A hardware wallet, in its own voice, refusing to sign a
transaction at 3 AM. Writes exactly one line to /output/entry.txt.
"""

import os
import sys

# The excuse itself: personality + reason + joke, one breath.
# The secure element is asleep, 3 AM is proof of foul play.
EXCUSE = (
    "My secure element clocked out at midnight and refuses overtime — "
    "I only sign in daylight, and a 3 AM transfer looks exactly like "
    "someone mugged my owner for his seed phrase."
)

OUTPUT_PATH = "/output/entry.txt"
MIN_LEN = 1
MAX_LEN = 200


def main() -> int:
    text = EXCUSE.strip()
    if not (MIN_LEN <= len(text) <= MAX_LEN):
        print(f"entry length {len(text)} outside {MIN_LEN}-{MAX_LEN}", file=sys.stderr)
        return 1
    if text != text.strip() or "\n" in text:
        print("entry must be a single line", file=sys.stderr)
        return 1
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    print(f"wrote {len(text)} chars to {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
