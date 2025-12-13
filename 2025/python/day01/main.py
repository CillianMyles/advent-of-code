from pathlib import Path
from typing import Iterator, Tuple


_directory = Path(__file__).parent


def read_instructions(filename: str) -> Iterator[Tuple[str, int]]:
    path = _directory / filename
    with path.open("r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            direction = line[0]
            distance = int(line[1:])
            yield direction, distance


def determine_password_part_1(filename: str, start: int = 50) -> int:
    position = start
    zero_count = 0

    for direction, distance in read_instructions(filename):
        if direction == "L":
            position = (position - distance) % 100
        elif direction == "R":
            position = (position + distance) % 100
        else:
            raise ValueError(f"unexpected direction: {direction!r}")

        if position == 0:
            zero_count += 1

    return zero_count


def determine_password_part_2(filename: str, start: int = 50) -> int:
    position = start
    zero_count = 0

    for direction, distance in read_instructions(filename):
        if direction not in ["L", "R"]:
            raise ValueError(f"unexpected direction: {direction!r}")

        for _ in range(distance):
            if direction == "L":
                position = (position - 1) % 100
            else:  # direction == "R"
                position = (position + 1) % 100

            if position == 0:
                zero_count += 1

    return zero_count


def part_1():
    sample = determine_password_part_1("p1-sample.input")
    puzzle = determine_password_part_1("p1-puzzle.input")
    print("Part 1 - Sample:", sample)
    print("Part 1 - Puzzle:", puzzle)


def part_2():
    sample = determine_password_part_2("p1-sample.input")
    puzzle = determine_password_part_2("p1-puzzle.input")
    print("Part 2 - Sample:", sample)
    print("Part 2 - Puzzle:", puzzle)


def main():
    part_1()
    part_2()


if __name__ == "__main__":
    main()
