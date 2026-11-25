#!/usr/bin/env python3
"""The Meeting That Should Have Been an Email.

The program writes a single line, one joke about a meeting that should
have been an email: an hour spent deciding the next meeting should have
been an email, followed by a follow-up to discuss it. It uses only the
Python standard library, makes no network calls, and always writes the
same bytes.
"""

import os

LINE = (
    "We held a one-hour meeting to decide that the next meeting should "
    "have been an email, then scheduled a follow-up to discuss it."
)

MAX_CHARS = 200


def main():
    assert "\n" not in LINE, "entry must be a single line"
    assert LINE.strip(), "entry must not be only whitespace"
    assert 1 <= len(LINE) <= MAX_CHARS, f"entry is {len(LINE)} chars, gate is 1-{MAX_CHARS}"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
