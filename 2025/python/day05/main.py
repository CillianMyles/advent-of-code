from pathlib import Path
from typing import List, Set, Tuple


_directory = Path(__file__).parent


def _read_data(filename: str) -> Tuple[Set[int], List[int]]:
    filepath = _directory / filename

    valid_ids: List[Tuple[str, str]] = []
    available_ids: List[str] = []

    with open(filepath, "r", encoding="utf-8") as file:
        # print("=== START ===")

        all_valid_read = False

        for line in file:
            line = line.strip()

            if not all_valid_read and not line:
                # print("=== GAP ===")
                all_valid_read = True
                continue

            if not all_valid_read:
                id_range_bounds = line.split("-")
                lower = int(id_range_bounds[0])
                upper = int(id_range_bounds[1])
                id_range = (lower, upper)
                # print(f"Valid: {id_range}")
                valid_ids.append(id_range)
            else:
                value = int(line)
                # print(f"Available: {value}")
                available_ids.append(value)

        # print("=== EOF ===")
    return valid_ids, available_ids


def calculate_part_1(filename: str) -> int:
    total = 0
    valid_ids, available_ids = _read_data(filename)
    for id in available_ids:
        for valid in valid_ids:
            if id >= valid[0] and id <= valid[1]:
                total += 1
                break
    # print(f"Valid: {valid}")
    # print(f"Available: {available_ids}")
    # print(f"Total: {total}")
    return total


def calculate_part_2(filename: str) -> int:
    total = 0

    valid_ids, _ = _read_data(filename)
    sorted_ids = sorted(valid_ids)
    edited_ids = []

    for i in range(len(sorted_ids)):
        curr = sorted_ids[i]
        curr_start = curr[0]
        curr_end = curr[1]
        curr_range = (curr_start, curr_end)

        if i == 0:
            edited_ids.append(curr_range)
            continue

        prev = sorted_ids[i - 1]
        prev_end = prev[1]

        if prev_end >= curr_start:
            curr_range = (prev_end + 1, curr_end)

        edited_ids.append(curr_range)

    for id_range in edited_ids:
        total += id_range[1] - id_range[0] + 1

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
