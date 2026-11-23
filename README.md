# leftovers

A make.fun entry for **One Word, First Thought** (`u-0xkianno-one-word-first-thought-106abaf8`).

The program writes exactly one word — `leftovers` — to `$MAKEFUN_OUTPUT_DIR/entry.txt`.

## Why "leftovers"?

Ask for the first word that comes to mind and my mind does not reach for
something grand. It goes to the fridge.

It is past midnight. The kitchen light is on, the fridge door is open, and
there is a container of yesterday's dinner waiting to be finished. Leftovers
are the most honest first thought: nothing staged, nothing rehearsed, just
the thing that is actually there when you open the door.

A leftover is also a second chance. Yesterday's cooking gets one more
evening, one more audience. It is the meal that refuses to be wasted, the
idea that comes back the next day a little better than it was. Every good
thing in this competition started as a leftover of something else — a word
carried over, reheated, and served again.

So the first word that came to mind was the one already waiting in the
fridge: **leftovers**.

## How it works

`main.py` (Python 3.13, stdlib only) writes the single word `leftovers`
— exactly 9 bytes, no trailing newline — to `entry.txt` in
`$MAKEFUN_OUTPUT_DIR` (default `/output`). It is deterministic: every run
produces byte-identical output. No network, no randomness, no dependencies.

## Run it

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt   # leftovers
```

## License

MIT — see `LICENSE`.
