#!/usr/bin/env python3
"""make.fun bounty: Make the AI Judge Laugh: Office Jokes.

The entry is one joke about office life, a single line of under 200
characters. This program writes it to /output/entry.txt.

It uses no network and is fully deterministic: every run writes the same
bytes. Output: UTF-8 text, 136 characters (gate: 1 to 199 characters).
The output file is left world-readable (mode 0644), as make.fun collects
it as another user.
"""
import os
import sys

JOKE = ("We switched to an open-plan office to improve communication \u2014 "
        "now everyone communicates exclusively through noise-cancelling "
        "headphones.")
DST = "/output/entry.txt"


def main() -> int:
    os.makedirs(os.path.dirname(DST), exist_ok=True)
    with open(DST, "w", encoding="utf-8") as f:
        f.write(JOKE)
    os.chmod(DST, 0o644)
    print(JOKE)
    print(f"wrote {DST} ({len(JOKE)} characters)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
