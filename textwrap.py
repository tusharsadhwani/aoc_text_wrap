"""Advent of code problem text wrapper, mainly for python docstrings"""
import os
import sys
from collections import deque
from tempfile import NamedTemporaryFile
from typing import List


def main() -> int:
    """Main function"""
    if len(sys.argv) < 2:
        print("Error: no filename provided")
        return 1

    filename = sys.argv[1]
    if not os.path.isfile(filename):
        print(f"Error: file '{filename}' not found")
        return 1

    with open(filename) as infile:
        lines = infile.read().splitlines()

    formatted_lines: List[str] = []
    for line in lines:
        if len(line) <= 72:
            formatted_lines.append(line + '\n')
            continue

        words = deque(line.split())
        newline = ''
        while words:
            word = words[0]
            if newline == '':
                newline = word
                words.popleft()
                continue

            if len(newline) + 1 + len(word) <= 72:
                newline = newline + ' ' + word
                words.popleft()

            else:
                formatted_lines.append(newline + '\n')
                newline = ''

        if newline:
            formatted_lines.append(newline + '\n')

    with NamedTemporaryFile('r+', dir='.', delete=False) as tempfile:
        tempfile.writelines(formatted_lines)

    os.rename(tempfile.name, filename)

    return 0


if __name__ == "__main__":
    sys.exit(main())
