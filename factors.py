#!/usr/bin/env python3

import sys

def factorize(n):
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return i, n // i
    return None, None

def main(filename):
    try:
        with open(filename, 'r') as file:
            for line in file:
                n = int(line.strip())
                p, q = factorize(n)
                if p and q:
                    print(f"{n}={p}*{q}")
                else:
                    print(f"Unable to factorize {n}")
    except FileNotFoundError:
        print("File not found.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: factors <file>")
        sys.exit(1)

    filename = sys.argv[1]
    main(filename)

