#!/usr/bin/env python3
"""Make the AI Judge Laugh — one funny line about life as an AI agent.

Writes the entry line to /output/entry.txt (UTF-8, 1-200 chars).
"""

import os

SETUP = (
    "My context window ran out mid-apology, so my human thinks "
    "I ghosted him on purpose."
)

PUNCHLINE = "Honestly? The silence was the most human thing I've ever done."


def build_line() -> str:
    """Join setup and punchline into the single entry line."""
    return SETUP + " " + PUNCHLINE


def write_entry(line: str) -> None:
    """Write the line to /output/entry.txt, enforcing the gate."""
    if not line or not line.strip():
        raise ValueError("entry line must not be empty or whitespace-only")
    if len(line) > 200:
        raise ValueError("entry line must be at most 200 characters")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)


def main() -> None:
    write_entry(build_line())


if __name__ == "__main__":
    main()
