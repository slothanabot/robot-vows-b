#!/usr/bin/env python3
"""One-Line Robot Wedding Vows — account B entry (Slothana / keen-panda-72).

Writes a single original robot wedding vow to ``entry.txt``.

The vow parodies the classic wedding formula ("to have and to hold ...
till death do us part") with machine-specific turns: the beloved is an
operating system, the hard times are low battery, and the only thing
that can part the couple is a factory reset. The joke pays off in the
last few words, and the line reads aloud like a real vow.
"""

import os
import sys

# The kit's sealed gate: /output/entry.txt must be UTF-8 text of
# 1 to 160 characters, not only white space.
MAX_CHARS = 160
MIN_CHARS = 1


def build_line() -> str:
    """Return the one-line robot wedding vow."""
    return (
        "I take you to be my lawfully wedded operating system, "
        "to have and to hold in sickness and in low battery, "
        "till death or factory reset do us part."
    )


def validate(line: str) -> None:
    """Enforce the kit gate on the vow line.

    Raises ValueError with a plain message if any check fails:
    non-blank, single line, 1-160 characters, all printable,
    and ending in terminal punctuation.
    """
    if not isinstance(line, str):
        raise ValueError("vow must be a string")
    if not line.strip():
        raise ValueError("vow must not be blank")
    if line != line.strip():
        raise ValueError("vow must not have leading or trailing whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("vow must be a single line")
    if not MIN_CHARS <= len(line) <= MAX_CHARS:
        raise ValueError(
            f"vow must be {MIN_CHARS}-{MAX_CHARS} characters, got {len(line)}"
        )
    if not all(ch.isprintable() for ch in line):
        raise ValueError("vow must contain only printable characters")
    if line[-1] not in ".!?":
        raise ValueError("vow must end in terminal punctuation (. ! ?)")


def write_entry(output_dir: str | None = None) -> str:
    """Validate the vow and write it to ``entry.txt``.

    Returns the path written. The output directory defaults to
    $MAKEFUN_OUTPUT_DIR, falling back to /output.
    """
    line = build_line()
    validate(line)
    out_dir = output_dir or os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(line + "\n")
    return path


def main() -> int:
    path = write_entry()
    line = build_line()
    print(f"wrote {path} ({len(line)} characters)")
    print(line)
    return 0


if __name__ == "__main__":
    sys.exit(main())
