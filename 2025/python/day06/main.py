from pathlib import Path
from typing import List, Tuple


_directory = Path(__file__).parent


def calculate_part_1(filename: str) -> int:
    return 0


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
