#!/usr/bin/env python3
"""Lucky Number — u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44.

Writes one original line of fortune-cookie wisdom for a software
developer to /output/entry.txt. Pure stdlib, no network.
Entry text: one original line (72 characters, single line).
"""

import os

TEXT = (
    "Your lucky number is the line count of the function "
    "you finally deleted."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
