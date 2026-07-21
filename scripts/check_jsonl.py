#!/usr/bin/env python3
"""Validate that each line of the given .jsonl files is valid JSON."""

import json
import sys


def main() -> int:
    exit_code = 0
    for path in sys.argv[1:]:
        with open(path, encoding="utf-8") as f:
            for line_no, line in enumerate(f, start=1):
                line = line.strip()
                if not line:
                    continue
                try:
                    json.loads(line)
                except json.JSONDecodeError as e:
                    print(f"{path}:{line_no}: invalid JSON: {e}")
                    exit_code = 1
    return exit_code


if __name__ == "__main__":
    sys.exit(main())
