from pathlib import Path
from typing import List, Tuple


_directory = Path(__file__).parent


def _read_data(filename: str) -> Tuple[List[Tuple[int, int]], List[int]]:
    filepath = _directory / filename

    valid_ids: List[Tuple[int, int]] = []
    available_ids: List[int] = []

    with open(filepath, "r", encoding="utf-8") as file:
        all_valid_read = False

        for line in file:
            line = line.strip()

            if not all_valid_read and not line:
                all_valid_read = True
                continue

            if not all_valid_read:
                bounds = line.split("-")
                lower = int(bounds[0])
                upper = int(bounds[1])
                valid_ids.append((lower, upper))

            else:
                value = int(line)
                available_ids.append(value)

    return valid_ids, available_ids


def calculate_part_1(filename: str) -> int:
    total = 0
    valid_ids, available_ids = _read_data(filename)

    for id in available_ids:
        for start, end in valid_ids:
            if start <= id <= end:
                total += 1
                break

    return total


def calculate_part_2(filename: str) -> int:
    total = 0
    valid_ids, _ = _read_data(filename)
    merged_ranges: List[Tuple[int, int]] = []

    for curr_start, curr_end in sorted(valid_ids):
        if not merged_ranges:
            merged_ranges.append((curr_start, curr_end))
            continue

        prev_start, prev_end = merged_ranges[-1]
        if curr_start <= prev_end:
            # overlapping ranges; merge them so IDs are only counted once
            merged_ranges[-1] = (prev_start, max(prev_end, curr_end))
        else:
            merged_ranges.append((curr_start, curr_end))

    for start, end in merged_ranges:
        total += end - start + 1

    return total


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
