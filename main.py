#!/usr/bin/env python3
"""Write one single-line joke excusing a missed deadline to /output/entry.txt."""

import os

ENTRY = "I missed the deadline because my to-do list filed a restraining order against me."
# One line, 81 characters: well under the 200-character cap, no trailing newline.


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
