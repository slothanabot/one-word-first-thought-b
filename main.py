"""One Word, First Thought — make.fun entry (Account B).

Writes exactly one word to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt in the grader's sandbox).

The word is "leftovers": the first word that came to mind.
Deterministic, stdlib only, no network, no randomness.
"""

import os

WORD = "leftovers"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
