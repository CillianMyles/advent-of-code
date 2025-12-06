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
    total_joltage = 0

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
        total_joltage += joltage

    return total_joltage


def calculate_part_2(filename: str) -> int:
    num_batteries = 12
    total_joltage = 0

    for l, line in enumerate(_read_lines(filename)):
        length = len(line)
        assert length >= num_batteries, "expected line to have at least 12 batteries"

        # print(f"Line: {line} - Length: {length}")

        candidates = []
        values = []

        for i in range(num_batteries):
            candidates.append(i)
            values.append(i)

        for i in range(length):
            if i < num_batteries:
                continue

            candidates.clear()
            for j in range(i - num_batteries, i):
                # print(f"[j={j}]")
                candidates.append(j)
            assert len(candidates) == num_batteries

            for j in range(len(candidates)):
                candidate = int(line[candidates[j]])
                value = int(line[values[j]])
                # print(f"[j={j}] - Candidate: {candidate} - Value: {value} - G: {candidate > value}")
                if candidate > value:
                    print(f"{candidate} > {value} - l:{l} - i:{i} - j:{j}")
                    for k in range(j, len(candidates)):
                        # print(f"[k={k}] - Candidate: {candidates[k]}")
                        values[k] = candidates[k]
            assert len(values) == num_batteries

            # print(f"[i={i}] - Candidates: {candidates} - Values: {values}")

        text = ""
        for index in values:
            text += line[index]

        total_joltage += int(text)
        # print(f"Answer: {text} - Values: {values}\n")

    return total_joltage


def part_1():
    sample = calculate_part_1("p1-sample.input")
    puzzle = calculate_part_1("p1-puzzle.input")
    print("Part 1 - Sample:", sample)
    print("Part 1 - Puzzle:", puzzle)


def part_2():
    sample = calculate_part_2("p1-sample.input")
    # puzzle = calculate_part_2("p1-puzzle.input")
    print("Part 2 - Sample:", sample)
    # print("Part 2 - Puzzle:", puzzle)


def main():
    # part_1()
    part_2()


if __name__ == "__main__":
    main()
