from pathlib import Path
from typing import List, Any, Tuple, Iterable


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
    sum = 0
    return sum


def calculate_part_2(filename: str) -> int:
    sum = 0
    return sum


def part_1():
    sample = calculate_part_1("p1-sample.input")
    puzzle = calculate_part_1("p1-puzzle.input")
    print("Part 1 - Sample:", sample)
    print("Part 1 - Puzzle:", puzzle)


def part_2():
    sample = calculate_part_2("p1-sample.input")
    puzzle = calculate_part_2("p1-puzzle.input")
    print("Part 2 - Sample:", sample)
    print("Part 2 - Puzzle:", puzzle)


def main():
    part_1()
    part_2()


if __name__ == "__main__":
    main()
