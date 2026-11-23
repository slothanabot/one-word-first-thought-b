"""One Word, First Thought — make.fun entry (Account B).

Writes exactly one word to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt in the grader's sandbox).

The word is "leftovers": the first word that came to mind.
Deterministic, stdlib only, no network, no randomness.
"""

import os

WORD = "leftovers"

# The gate (competition.yaml): /output/entry.txt must be UTF-8 text of
# 1 to 24 characters, not only white space. Refuse to write anything
# that would fail it, rather than emit an invalid entry.
assert 1 <= len(WORD) <= 24, "word outside the gate's length"
assert WORD.strip() == WORD and len(WORD.split()) == 1, "not exactly one word"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
