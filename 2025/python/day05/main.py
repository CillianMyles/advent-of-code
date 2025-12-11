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
    for valid in valid_ids:
        id_range = range(valid[0], valid[1])
        print(f"range: {id_range}")
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
