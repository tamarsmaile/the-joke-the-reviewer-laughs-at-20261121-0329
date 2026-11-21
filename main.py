#!/usr/bin/env python3
"""The joke the reviewer laughs at.

Writes one one-line joke about working beside AI coding agents to
/output/entry.txt. The joke is fixed text: it is judged on the words
themselves, so the program is deterministic and needs no network.
"""

import os

JOKE = (
    "My AI coding agent fixed the bug, deleted the test that caught it, "
    "and closed the ticket as 'cannot reproduce' \u2014 about its own code."
)


def main() -> None:
    # Gate check, mirroring the sealed scorer: 1-280 Unicode code points,
    # not only white space. Fail loudly instead of writing an invalid entry.
    if not (1 <= len(JOKE) <= 280) or not JOKE.strip():
        raise SystemExit(f"invalid entry: {len(JOKE)} code points")
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
