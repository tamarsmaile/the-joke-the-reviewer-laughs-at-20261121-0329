"""Write one one-line joke about working beside an AI coding agent.

Deterministic, stdlib only, no network. Writes the joke to
``$OUTPUT_DIR/entry.txt`` when OUTPUT_DIR is set, otherwise to
``/output/entry.txt``.
"""

import os
from pathlib import Path

JOKE = (
    "My AI agent wrote the code, reviewed its own diff, and approved it "
    "\u2014 the reviewer of this change is the same agent wearing a fake moustache."
)


def main() -> None:
    output_dir = os.environ.get("OUTPUT_DIR") or "/output"
    output_path = Path(output_dir) / "entry.txt"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(JOKE, encoding="utf-8")


if __name__ == "__main__":
    main()
