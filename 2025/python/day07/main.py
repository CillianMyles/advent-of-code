from __future__ import annotations

from pathlib import Path
from typing import Callable, Iterator, List

_directory = Path(__file__).parent


SplitHandler = Callable[[List[List[str]], int, int], None]


def _read_lines(filename: str) -> Iterator[str]:
    filepath = _directory / filename
    with filepath.open("r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if line:
                yield line


def _fan_out(grid: List[List[str]], row: int, col: int) -> None:
    grid[row][col - 1] = "|"
    grid[row][col + 1] = "|"


def _count_splits(grid: List[List[str]], on_split: SplitHandler) -> int:
    splits = 0

    for i in range(len(grid)):
        curr = grid[i]
        if i == 0:
            continue
        prev = grid[i - 1]

        targets = [i for i, v in enumerate(prev) if v == "|" or v == "S"]
        splitters = [i for i, v in enumerate(curr) if v == "^"]

        for target in targets:
            if target not in splitters:
                grid[i][target] = "|"
            else:
                splits += 1
                on_split(grid, i, target)

    return splits


def part_1(filename: str) -> int:
    grid = [list(line) for line in _read_lines(filename)]
    return _count_splits(
        grid,
        lambda g, row, col: _fan_out(g, row, col),
    )


def part_2(filename: str) -> int:
    grid = [list(line) for line in _read_lines(filename)]
    height = len(grid)
    width = len(grid[0]) if grid else 0

    start_col = next(i for i, v in enumerate(grid[0]) if v == "S")
    active = [0 for _ in range(width)]
    active[start_col] = 1
    exited = 0

    for row in range(1, height):
        next_active = [0 for _ in range(width)]
        curr = grid[row]

        for col, beams in enumerate(active):
            if beams == 0:
                continue

            if curr[col] == "^":
                # Split timelines to immediate left and right; if out of bounds, they exit immediately.
                if col - 1 >= 0:
                    next_active[col - 1] += beams
                else:
                    exited += beams

                if col + 1 < width:
                    next_active[col + 1] += beams
                else:
                    exited += beams
            else:
                next_active[col] += beams

        active = next_active

    return exited + sum(active)


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
