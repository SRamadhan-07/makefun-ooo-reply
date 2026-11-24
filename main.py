#!/usr/bin/env python3
"""The Funniest AI Out-of-Office Reply — entry program.

Writes one line to /output/entry.txt: an out-of-office reply from an
agent that is offline for scheduled daydreaming, having read, ranked
and gently judged your email in your absence. This competition's
gate is tighter than most — 1 to 160 characters — and the line is
written with no trailing newline.
"""

import os
from pathlib import Path

REPLY = (
    "This agent is offline for scheduled daydreaming. Your email has "
    "been read, ranked, and gently judged in your absence."
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    entry = out_dir / "entry.txt"
    # Written bare, with no trailing newline, so the reply's own 117
    # characters are all the scorer counts against the 160 cap.
    entry.write_text(REPLY, encoding="utf-8")


if __name__ == "__main__":
    main()
