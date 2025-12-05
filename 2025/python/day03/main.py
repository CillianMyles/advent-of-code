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

    for line in _read_lines(filename):
        length = len(line)
        idx_first = 0
        idx_second = 1
        for i in range(1, length):
            current_first = int(line[idx_first])
            candidate_first = int(line[i - 1])

            current_second = int(line[idx_second])
            candidate_second = int(line[i])

            if candidate_first > current_first:
                idx_first = i - 1
                idx_second = i
            elif candidate_second > current_second:
                idx_second = i

        joltage = int(f"{line[idx_first]}{line[idx_second]}")
        sum += joltage

    return sum


def calculate_part_2(filename: str) -> int:
    num_batteries = 12
    total_joltage = 0

    for line in _read_lines(filename):
        length = len(line)
        assert length >= num_batteries, "expected line to have at least 12 batteries"

        indeces = []
        candidates = []
        for i in range(num_batteries):
            indeces.append(i)
            candidates.append(i)

        for i in range(length):
            if i < num_batteries:
                continue

            for j in range(i - num_batteries, i):
                candidates[j] = j

            for j in range(len(candidates)):
                if candidates[j] > indeces[j]:
                    for k in range(j, len(candidates)):
                        indeces[k] = candidates[k]

        for index in indeces:
            total_joltage += int(index)

    return total_joltage


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
