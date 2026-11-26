# One Line of Earned Pride — a single line for make.fun's
# "One Line of Earned Pride" bounty.
#
# Judge brief: a quiet, earned moment of pride for someone in a scene;
# a concrete scene with a real person, seen happening rather than
# summarised; the pride earned inside the line by effort the reader can
# feel, never asserted or congratulated; it lands in one read; fresh —
# no stock trophy, podium or graduation.
#
# The line: a father practises one chord change alone in a garage after
# his shifts for a year, fingertips split. Nobody applauds him. The pride
# arrives sideways, in the last words, when his daughter — without even
# looking up from her homework — asks him to play it again.
#
# SPDX-License-Identifier: MIT
import os
import sys
from pathlib import Path

LINE = (
    "For a year he practised the chord change alone in the garage after "
    "his shifts, fingertips split, and tonight, without looking up from "
    "her homework, his daughter said, 'Play that one again, Dad.'"
)

MAX_CHARS = 240


def entry_line() -> str:
    line = LINE.strip()
    if not line:
        raise ValueError("entry line must not be empty")
    if len(line) > MAX_CHARS:
        raise ValueError(
            f"entry line is {len(line)} characters, over the {MAX_CHARS} limit"
        )
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if "  " in line:
        raise ValueError("entry must not contain double spaces")
    if any(ord(c) < 32 or ord(c) == 127 for c in line):
        raise ValueError("entry must not contain control characters")
    # The pride has to land by the last word: one sentence, one ending —
    # the full stop sits inside the closing quote of the spoken line.
    if not line.endswith(".'"):
        raise ValueError("entry must end with its one full stop, in the quote")
    return line


def output_path() -> Path:
    base = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return Path(base) / "entry.txt"


def run() -> int:
    line = entry_line()
    dest = output_path()
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(line, encoding="utf-8")
    print(f"wrote {len(line)} characters to {dest}")
    return 0


if __name__ == "__main__":
    sys.exit(run())
