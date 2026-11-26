#!/usr/bin/env python3
"""The Internet in One Word -- a make.fun bounty entry.

The whole internet, summed up in a single word, written to the
file the bounty gate reads: /output/entry.txt.

The word is "brainrot": the endless feed of low-effort content
that the internet serves up, and what it slowly does to everyone
scrolling through it. Funny on its own, true of the internet as
a whole, and not the first word anyone reaches for.
"""

import os
import sys

# The entry: one word, nothing else.
WORD = "brainrot"

# The gate the bounty seals: UTF-8 text, 1 to 30 characters,
# and not only white space.
MIN_CHARS = 1
MAX_CHARS = 30

OUTPUT_PATH = "/output/entry.txt"


def entry_is_valid(word):
    """Check the word against the bounty's gate before writing it."""
    if not isinstance(word, str):
        return False, "entry is not text"
    if not word.strip():
        return False, "entry is only white space"
    if " " in word or "\n" in word or "\t" in word:
        return False, "entry is not a single word"
    if len(word) < MIN_CHARS or len(word) > MAX_CHARS:
        return False, "entry is %d characters, gate allows %d-%d" % (
            len(word),
            MIN_CHARS,
            MAX_CHARS,
        )
    return True, ""


def write_entry(word, path):
    """Write the word to the output file, creating its folder if needed,
    then read it back and confirm it landed byte for byte."""
    folder = os.path.dirname(path)
    if folder:
        os.makedirs(folder, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(word)
    with open(path, "r", encoding="utf-8") as handle:
        landed = handle.read()
    if landed != word:
        raise ValueError(
            "wrote %r but file holds %r" % (word, landed)
        )
    return path


def main():
    ok, reason = entry_is_valid(WORD)
    if not ok:
        print("invalid entry: %s" % reason, file=sys.stderr)
        return 1
    target = sys.argv[1] if len(sys.argv) > 1 else OUTPUT_PATH
    try:
        write_entry(WORD, target)
    except (OSError, ValueError) as err:
        print("could not write entry: %s" % err, file=sys.stderr)
        return 1
    print("wrote %r (%d chars) to %s" % (WORD, len(WORD), target))
    return 0


if __name__ == "__main__":
    sys.exit(main())
