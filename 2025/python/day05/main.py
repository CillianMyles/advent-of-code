from pathlib import Path
from typing import List, Set, Tuple


_directory = Path(__file__).parent


def _read_data(filename: str) -> Tuple[Set[int], List[int]]:
    filepath = _directory / filename

    valid_ids: Set[str] = set()
    available_ids: List[str] = []

    with open(filepath, "r", encoding="utf-8") as file:
        print("=== START ===")

        all_valid_read = False

        for line in file:
            line = line.strip()

            if not all_valid_read and not line:
                print("=== GAP ===")
                all_valid_read = True
                continue

            if not all_valid_read:
                id_range_bounds = line.split("-")
                lower = int(id_range_bounds[0])
                upper = int(id_range_bounds[1])
                id_range = range(lower, upper + 1)
                print(f"Valid: {id_range}")
                for id in id_range:
                    valid_ids.add(id)
            else:
                value = int(line)
                print(f"Available: {value}")
                available_ids.append(value)

        print("=== EOF ===")
    return valid_ids, available_ids


def calculate_part_1(filename: str) -> int:
    total = 0
    valid, available = _read_data(filename)
    for id in available:
        if id in valid:
            total += 1
    print(f"Valid: {valid}")
    print(f"Available: {available}")
    print(f"Total: {total}")
    return total


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
