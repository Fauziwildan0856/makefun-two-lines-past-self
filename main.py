"""Two Lines to Your Past Self -- make.fun entry.

Writes a two-line warning to the writer's past self to
MAKEFUN_OUTPUT_DIR/entry.txt (or /output/entry.txt when the
variable is unset). Standard library only.

Judge brief, in short: line 1 warns the past self about ONE
specific moment in a single sentence -- a time, a place, a
decision, or words said out loud, vivid enough to picture.
Line 2 says in one sentence why that moment mattered and what
changed because of it: real cause and effect, not a repeat of
line 1, in a plain voice written to one specific person.
"""

import os
from pathlib import Path

ENTRY = (
    "Don't tap send on that text at 2 in the morning from the bus "
    "stop on Jalan Sudirman, the one that says you're done with her.\n"
    "She believed you, and the next three years of your life went "
    "quiet in a way no apology ever filled back in."
)


def check_entry(text: str) -> None:
    """Check the entry against the kit gate and the judge brief
    before writing anything.

    The sealed scorer requires UTF-8 text of 1-280 characters
    that is not only whitespace; the judge brief additionally
    requires exactly two lines, each a single sentence.
    """
    if not 1 <= len(text) <= 280:
        raise SystemExit(
            f"entry fails the kit gate: {len(text)} characters "
            "(must be 1-280)"
        )
    if not text.strip():
        raise SystemExit("entry fails the kit gate: only whitespace")
    lines = text.split("\n")
    if len(lines) != 2:
        raise SystemExit(
            f"entry fails the judge brief: {len(lines)} lines, "
            "expected exactly 2"
        )
    for i, line in enumerate(lines, start=1):
        # One sentence means exactly one sentence terminator, and
        # it must close the line: a second terminator would mean
        # a second sentence crowding the line. The offending line
        # is shown so a failed check is easy to trace.
        terminators = sum(line.count(mark) for mark in ".!?")
        if terminators != 1 or line[-1] not in ".!?":
            raise SystemExit(
                f"entry fails the judge brief: line {i} is not "
                f"exactly one sentence: {line!r}"
            )


def main() -> None:
    check_entry(ENTRY)
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_text(ENTRY, encoding="utf-8")
    print(f"Wrote {len(ENTRY)} characters to {target}")


if __name__ == "__main__":
    main()
