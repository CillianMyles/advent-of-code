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


def _split_left(grid: List[List[str]], row: int, col: int) -> None:
    grid[row][col - 1] = "|"


def _split_right(grid: List[List[str]], row: int, col: int) -> None:
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
    total = 0
    grid = [list(line) for line in _read_lines(filename)]
    left = grid.copy()
    right = grid.copy()

    left_splits = _count_splits(
        left,
        lambda g, row, col: _split_left(g, row, col),
    )
    total += left_splits

    right_splits = _count_splits(
        right,
        lambda g, row, col: _split_right(g, row, col),
    )
    total += right_splits

    for i, l in enumerate(left):
        print(f"[{i}] {l}")

    for i, r in enumerate(right):
        print(f"[{i}] {r}")

    print(f"left: {left_splits} - right - {right_splits}")
    return total


def main() -> None:
    sample_1 = part_1("p1-sample.input")
    print(f"Part 1 - Sample: {sample_1}")
    puzzle_1 = part_1("p1-puzzle.input")
    print(f"Part 1 - Puzzle: {puzzle_1}")

    sample_2 = part_2("p1-sample.input")
    print(f"Part 2 - Sample: {sample_2}")
    # puzzle_2 = part_2("p1-puzzle.input")
    # print(f"Part 2 - Puzzle: {puzzle_2}")


if __name__ == "__main__":
    main()
