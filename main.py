"""One Word From Your Ex -- make.fun entry.

Writes the single word the entrant's ex would use to describe them
to /output/entry.txt. Standard library only.
"""

import os
import sys

# The word: "almost" -- as in "he was almost the one."
# One small word carrying a whole relationship that never quite arrived.
WORD = "almost"


def main() -> int:
    # Self-check against the sealed gate: 1-24 UTF-8 characters,
    # not only whitespace.
    if not 1 <= len(WORD) <= 24:
        print(f"entry must be 1-24 characters, got {len(WORD)}", file=sys.stderr)
        return 1
    if not WORD.strip():
        print("entry must not be only whitespace", file=sys.stderr)
        return 1
    out_path = "/output/entry.txt"
    os.makedirs("/output", exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(WORD)
    print(f"wrote {len(WORD)} characters to {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
