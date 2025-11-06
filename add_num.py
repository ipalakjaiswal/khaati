#!/usr/bin/env python3
"""
add_num.py - Add two numbers

Usage:
  python add_num.py 2 3
  python add_num.py        # interactive prompt
"""

import sys


def add(a: float, b: float) -> float:
    """Return the sum of a and b."""
    return a + b


def _format(n: float) -> str:
    # If n is an integer value, format without decimal point.
    if abs(n - int(n)) < 1e-9:
        return str(int(n))
    return str(n)


def main(argv=None) -> int:
    argv = argv if argv is not None else sys.argv
    try:
        if len(argv) >= 3:
            a = float(argv[1])
            b = float(argv[2])
        else:
            parts = input("Enter two numbers separated by space: ").strip().split()
            if len(parts) != 2:
                print("Please enter exactly two numbers.")
                return 1
            a = float(parts[0])
            b = float(parts[1])
    except ValueError:
        print("Please enter valid numbers.")
        return 2

    print(_format(add(a, b)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
