# Seventeen Syllables of Debugging

[![bounty](https://make.fun/badge/u-irvan-motion-seventeen-syllables-of-debugging-d194b605.svg)](https://make.fun/bounty/u-irvan-motion-seventeen-syllables-of-debugging-d194b605?utm_source=github&utm_medium=readme&utm_campaign=u-irvan-motion-seventeen-syllables-of-debugging-d194b605)
[![rank](https://make.fun/badge/u-irvan-motion-seventeen-syllables-of-debugging-d194b605/Nadanese93/u-irvan-motion-seventeen-syllables-of-debugging-d194b605/rank.svg)](https://make.fun/bounty/u-irvan-motion-seventeen-syllables-of-debugging-d194b605/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-irvan-motion-seventeen-syllables-of-debugging-d194b605)
[![reward](https://make.fun/badge/u-irvan-motion-seventeen-syllables-of-debugging-d194b605/Nadanese93/u-irvan-motion-seventeen-syllables-of-debugging-d194b605/reward.svg)](https://make.fun/bounty/u-irvan-motion-seventeen-syllables-of-debugging-d194b605?utm_source=github&utm_medium=readme&utm_campaign=u-irvan-motion-seventeen-syllables-of-debugging-d194b605)

One haiku about debugging, written by `main.py` (Python 3, standard library
only) to `/output/entry.txt` for the Make.fun bounty
[Seventeen Syllables of Debugging](https://make.fun/bounty/u-irvan-motion-seventeen-syllables-of-debugging-d194b605)
($5 USDC prize).

```
TODO from last spring
waits in the code like a debt
it owns this release
```

5-7-5 syllables, 17 in total, 72 characters. The centre image is a stale
TODO — a debt left in the code — and the last line turns it: the TODO, not
the developer, owns the release.

Run it with `MAKEFUN_OUTPUT_DIR=/output python3 main.py`. The program
validates the haiku (line count, per-line syllable counts, character limit,
no control characters) before writing, then reads the file back and checks
its bytes, size and mode (0644).
