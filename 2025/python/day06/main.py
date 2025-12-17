from __future__ import annotations

from math import prod
from pathlib import Path
from typing import Iterable, Iterator

_directory = Path(__file__).parent


def _read_lines(filename: str) -> Iterator[str]:
    filepath = _directory / filename
    with filepath.open("r", encoding="utf-8") as file:
        for line in file:
            line = line.rstrip("\n")
            if line:
                yield line


def _eval(sign: str, values: Iterable[int]) -> int:
    values = list(values)
    if sign == "+":
        return sum(values)
    if sign == "*":
        return prod(values)
    raise ValueError(f"unexpected sign: {sign}")


def part_1(filename: str) -> int:
    rows = [line.split() for line in _read_lines(filename)]
    if not rows:
        return 0

    width = len(rows[0])
    if any(len(r) != width for r in rows):
        raise ValueError("unexpected parts length")

    total = 0
    for block in zip(*rows):
        *nums, sign = block
        total += _eval(sign, (int(n) for n in nums))
    return total


def _sign_spans(line: str) -> list[tuple[int, int, str]]:
    """
    Returns [(start_idx, end_idx, sign_char), ...] in left-to-right order,
    where end_idx is inclusive.
    """
    positions = [(i, ch) for i, ch in enumerate(line) if ch != " "]
    if not positions:
        return []

    width = len(line)
    spans: list[tuple[int, int, str]] = []
    for idx, (start, sign) in enumerate(positions):
        end = (positions[idx + 1][0] - 1) if idx + 1 < len(positions) else (width - 1)
        spans.append((start, end, sign))
    return spans


def _vertical_numbers(lines: list[str], start: int, end: int) -> list[int]:
    """
    Scans columns from end..start (right-to-left) and builds numbers vertically.
    Each column contributes 0..1 digit per row; digits are concatenated top-down.
    """
    nums: list[int] = []
    for col in range(end, start - 1, -1):
        val = "".join(line[col] for line in lines if line[col] != " ")
        if val:
            nums.append(int(val))
    return nums


def part_2(filename: str) -> int:
    lines = list(_read_lines(filename))
    if not lines:
        return 0

    total = 0
    signs_line = lines.pop()
    for start, end, sign in reversed(_sign_spans(signs_line)):
        values = _vertical_numbers(lines, start, end)
        total += _eval(sign, values)
    return total


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
