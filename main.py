#!/usr/bin/env python3
"""Write one haiku about debugging to /output/entry.txt.

Haiku (5-7-5, 17 syllables, 72 characters, no trailing newline):
    TODO from last spring
    waits in the code like a debt
    it owns this release
"""
import os
import stat

HAIKU = (
    "TODO from last spring\n"
    "waits in the code like a debt\n"
    "it owns this release"
)

# Syllable counts per word, for the words used in this haiku only.
SYLLABLES = {
    "todo": 2, "from": 1, "last": 1, "spring": 1,
    "waits": 1, "in": 1, "the": 1, "code": 1, "like": 1, "a": 1, "debt": 1,
    "it": 1, "owns": 1, "this": 1, "release": 2,
}
EXPECTED_LINES = (5, 7, 5)


def count_syllables(line):
    total = 0
    for word in line.split():
        key = word.strip(".,;:!?").lower()
        if key not in SYLLABLES:
            raise ValueError("unknown word for syllable count: %r" % word)
        total += SYLLABLES[key]
    return total


def validate(text):
    if not text or not text.strip():
        raise ValueError("entry is empty or whitespace-only")
    if len(text) > 200:
        raise ValueError("entry exceeds 200 characters: %d" % len(text))
    if not text.isascii():
        raise ValueError("entry must be plain ASCII text")
    if any(ord(ch) < 32 and ch != "\n" for ch in text):
        raise ValueError("entry contains control characters")
    if "\r" in text or "\t" in text or chr(127) in text:
        raise ValueError("entry contains carriage return, tab or DEL")
    if text != text.strip():
        raise ValueError("entry has leading or trailing whitespace")
    lines = text.split("\n")
    if len(lines) != 3:
        raise ValueError("entry must have exactly 3 lines, got %d" % len(lines))
    for line, expected in zip(lines, EXPECTED_LINES):
        got = count_syllables(line)
        if got != expected:
            raise ValueError(
                "line %r has %d syllables, expected %d" % (line, got, expected)
            )
    return True


def main():
    validate(HAIKU)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    data = HAIKU.encode("utf-8")
    with open(path, "wb") as f:
        f.write(data)
    os.chmod(path, 0o644)
    # Read-back check: bytes, size and mode must match what was written.
    with open(path, "rb") as f:
        back = f.read()
    if back != data:
        raise ValueError("read-back bytes differ from written bytes")
    if len(back) != 72 or os.path.getsize(path) != 72:
        raise ValueError("read-back size %d, expected 72" % len(back))
    if back.endswith(b"\n"):
        raise ValueError("entry must not end with a trailing newline")
    mode = stat.S_IMODE(os.stat(path).st_mode)
    if mode != 0o644:
        raise ValueError("entry.txt mode %o, expected 644" % mode)
    decoded = back.decode("utf-8")
    validate(decoded)
    counts = [count_syllables(line) for line in decoded.split("\n")]
    if tuple(counts) != EXPECTED_LINES:
        raise ValueError("read-back syllable counts %r, expected %r"
                         % (counts, EXPECTED_LINES))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
