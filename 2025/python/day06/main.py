from math import prod
from pathlib import Path
from typing import Iterator, List, Tuple


_directory = Path(__file__).parent


def _read_lines(filename: str) -> Iterator[str]:
    filepath = _directory / filename
    with open(filepath, "r", encoding="utf-8") as file:
        for line in file:
            line = line.rstrip("\n")
            if not line:
                continue
            yield line


def part_1(filename: str) -> int:
    total = 0
    data: List[List[str]] = []
    num_parts: int | None = None

    for line in _read_lines(filename):
        parts = line.split()

        if num_parts is None:
            num_parts = len(parts)
            for i in range(num_parts):
                data.insert(i, [])
        else:
            assert num_parts == len(parts), "unexpected parts length"

        for i, part in enumerate(parts):
            data[i].append(part)

    for block in data:
        sign = block.pop(-1)
        values = [int(v) for v in block]
        if sign == "+":
            total += sum(values)
        elif sign == "*":
            total += prod(values)
        else:
            raise ValueError(f"unexpected sign: {sign}")

    return total


def part_2(filename: str) -> int:
    total = 0

    lines = [line for line in _read_lines(filename)]

    signs: List[Tuple[int, str]] = []
    last = lines.pop(-1)
    for i, char in enumerate(last):
        if char != " ":
            signs.append((i, char))

    width = len(last)
    for i in range(len(signs) - 1, -1, -1):
        start, sign = signs[i]
        if i == len(signs) - 1:
            end = width - 1
        else:
            end = signs[i + 1][0] - 1
        length = end - start + 1
        rows: List[str] = ["" for _ in range(length)]
        idx = 0
        for j in range(end, start - 1, -1):
            for k in range(len(lines)):
                line = lines[k]
                val = line[j]
                if val != " ":
                    rows[idx] += val
            idx += 1

        values = []
        for row in rows:
            if row:
                values.append(int(row))
        if sign == "+":
            total += sum(values)
        elif sign == "*":
            total += prod(values)
        else:
            raise ValueError(f"unexpected sign: {sign}")

    return total


def main():
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
