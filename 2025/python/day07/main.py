from __future__ import annotations

from math import prod
from pathlib import Path
from typing import Iterable, Iterator, List

_directory = Path(__file__).parent


def _read_lines(filename: str) -> Iterator[str]:
    filepath = _directory / filename
    with filepath.open("r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if line:
                yield line


def part_1(filename: str) -> int:
    splits = 0
    start: int | None = None
    grid = [list(line) for line in _read_lines(filename)]

    for i in range(len(grid)):
        curr = grid[i]

        if i == 0:
            start = curr.index("S")
            print(f'[0] "S" found at {start}')
            continue

        if i == 1:
            if curr[start] == ".":
                grid[i][start] = "|"
                continue
            else:
                raise Exception("expected (.) below (S)")

        prev = grid[i - 1]
        beams = [i for i, v in enumerate(prev) if v == "|"]
        markers = [i for i, v in enumerate(curr) if v == "^"]
        # print(f"[{i}] - beams (|): {beams} - markers (^): {markers}")

        for beam in beams:
            if beam not in markers:
                grid[i][beam] = "|"
            else:
                splits += 1
                grid[i][beam - 1] = "|"
                grid[i][beam + 1] = "|"

    for j, line in enumerate(grid):
        print(f"[{j}] {line}")

    return splits


def part_2(filename: str) -> int:
    return 0


def main() -> None:
    sample_1 = part_1("p1-sample.input")
    print(f"Part 1 - Sample: {sample_1}")
    puzzle_1 = part_1("p1-puzzle.input")
    print(f"Part 1 - Puzzle: {puzzle_1}")

    sample_2 = part_2("p1-sample.input")
    print(f"Part 2 - Sample: {sample_2}")
    puzzle_2 = part_2("p1-puzzle.input")
    print(f"Part 2 - Puzzle: {puzzle_2}")


if __name__ == "__main__":
    main()
