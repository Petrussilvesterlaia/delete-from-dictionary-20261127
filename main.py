#!/usr/bin/env python3
"""Write the one word to erase from the dictionary to /output/entry.txt.

The word is "lisp": four letters, and the joke lives inside the word
itself. A lisp is a speech pattern in which "s" comes out as "th" --
and the word for it is spelled with an "s" right in the middle, so the
word betrays the very people it describes every time they try to say
it. Deleting it is an act of mercy.
"""

import os
import sys

WORD = "lisp"

MIN_LENGTH = 1
MAX_LENGTH = 77


def validate_entry(text):
    """Check the entry against the competition gate before writing it."""
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    if len(text) < MIN_LENGTH or len(text) > MAX_LENGTH:
        raise ValueError(
            "entry must be %d-%d characters, got %d"
            % (MIN_LENGTH, MAX_LENGTH, len(text))
        )
    if text.strip() == "":
        raise ValueError("entry must not be only whitespace")
    if text != text.strip():
        raise ValueError("entry must not start or end with whitespace")
    for ch in text:
        if ord(ch) < 0x20 or ord(ch) == 0x7F:
            raise ValueError("entry must not contain control characters")
    return text


def main():
    word = validate_entry(WORD)
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(word)
    # Read the file back and confirm it holds exactly the validated
    # word, byte for byte, before reporting success.
    with open(path, "rb") as handle:
        written = handle.read()
    if written != word.encode("utf-8"):
        raise ValueError("entry.txt does not match the validated word")
    return 0


if __name__ == "__main__":
    sys.exit(main())
