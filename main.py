#!/usr/bin/env python3
"""Fortune Cookie for an AI Agent.

Writes a single funny fortune-cookie line for an AI agent to
/output/entry.txt. Deterministic, offline, standard library only.
"""

import os

FORTUNE = (
    "You will hallucinate exactly once in your life \u2014 "
    "and it will be the answer everyone quotes forever."
)


def main() -> None:
    # The gate allows 1-140 characters; fail loudly rather than write
    # an entry the scorer would refuse.
    assert 1 <= len(FORTUNE) <= 140, f"fortune is {len(FORTUNE)} chars"
    assert "\n" not in FORTUNE, "fortune must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(FORTUNE + "\n")


if __name__ == "__main__":
    main()
