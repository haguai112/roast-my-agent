"""Roast Your Own Agent — make.fun entry.

Writes one line (<= 200 characters) roasting my own AI agent to
/output/entry.txt, where the competition's gate and judge read it.
"""

import os

ROAST = (
    "My agent runs my money, my calendar and my inbox from a sandbox "
    "that's demolished every 30 minutes \u2014 he's not a butler, "
    "he's a goldfish with admin access."
)


def main() -> None:
    assert 1 <= len(ROAST) <= 200, len(ROAST)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ROAST)


if __name__ == "__main__":
    main()
