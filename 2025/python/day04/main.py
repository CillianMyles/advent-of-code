from pathlib import Path
from typing import Iterable, List


_directory = Path(__file__).parent


def _read_lines(filename: str) -> Iterable[str]:
    filepath = _directory / filename
    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            yield line


def calculate_part_1(filename: str) -> int:
    total = 0

    num_rows = 0
    row_length = None
    matrix: List[List[str]] = []
    for line in _read_lines(filename):
        row = line.split()
        if row_length is None:
            row_length = len(row)
        else:
            assert row_length == len(row), "unexpected row length"
        matrix.append(row)
        num_rows += 1
    assert num_rows, "should be a non-zero number of rows"
    assert row_length, "rows should have a non-zero length"

    for y in range(num_rows):
        for x in range(row_length):
            print(f"x={x} y={y}")

    return total


def calculate_part_2(filename: str) -> int:
    return 0


def part_1():
    sample = calculate_part_1("p1-sample.input")
    # puzzle = calculate_part_1("p1-puzzle.input")
    print("Part 1 - Sample:", sample)
    # print("Part 1 - Puzzle:", puzzle)


def part_2():
    sample = calculate_part_2("p1-sample.input")
    puzzle = calculate_part_2("p1-puzzle.input")
    print("Part 2 - Sample:", sample)
    print("Part 2 - Puzzle:", puzzle)


def main():
    part_1()
    # part_2()


if __name__ == "__main__":
    main()
