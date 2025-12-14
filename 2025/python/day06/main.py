from math import prod
from pathlib import Path
from typing import Iterator, List


_directory = Path(__file__).parent


def _read_lines(filename: str) -> Iterator[str]:
    filepath = _directory / filename
    with open(filepath, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            yield line


def calculate_part_1(filename: str) -> int:
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

    for row in data:
        sign = row[len(row) - 1]
        values = [int(value) for value in row[:-1]]
        if sign == "+":
            total += sum(values)
        elif sign == "*":
            total += prod(values)
        else:
            raise ValueError(f"unexpected sign: {sign}")

    return total


def calculate_part_2(filename: str) -> int:
    return 0


def part_1():
    sample = calculate_part_1("p1-sample.input")
    print("Part 1 - Sample:", sample)
    puzzle = calculate_part_1("p1-puzzle.input")
    print("Part 1 - Puzzle:", puzzle)


def part_2():
    sample = calculate_part_2("p1-sample.input")
    print("Part 2 - Sample:", sample)
    puzzle = calculate_part_2("p1-puzzle.input")
    print("Part 2 - Puzzle:", puzzle)


def main():
    part_1()
    part_2()


if __name__ == "__main__":
    main()
