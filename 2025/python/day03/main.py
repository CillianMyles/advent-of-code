from pathlib import Path
from typing import Iterator


_directory = Path(__file__).parent


def _read_lines(filename: str) -> Iterator[str]:
    filepath = _directory / filename
    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            yield line


def _calculate_total_joltage(filename: str, num_batteries: int) -> int:
    total_joltage = 0

    for line in _read_lines(filename):
        length = len(line)
        assert length >= num_batteries, "line legnth shorter than expected"

        candidates = []
        values = []

        for i in range(num_batteries):
            candidates.append(i)
            values.append(i)

        for i in range(length):
            if i < num_batteries:
                continue

            candidates.clear()
            for j in range(i - num_batteries + 1, i + 1):
                candidates.append(j)
            assert len(candidates) == num_batteries

            for j in range(len(candidates)):
                candidate = int(line[candidates[j]])
                value = int(line[values[j]])
                if candidate > value:
                    for k in range(j, len(candidates)):
                        values[k] = candidates[k]
            assert len(values) == num_batteries

        text = ""
        for index in values:
            text += line[index]

        total_joltage += int(text)

    return total_joltage


def calculate_part_1(filename: str) -> int:
    return _calculate_total_joltage(
        filename=filename,
        num_batteries=2,
    )


def calculate_part_2(filename: str) -> int:
    return _calculate_total_joltage(
        filename=filename,
        num_batteries=12,
    )


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
