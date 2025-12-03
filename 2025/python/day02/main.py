from pathlib import Path
from typing import List, Any, Tuple


_directory = Path(__file__).parent


def _load_ids(file: str) -> List[Tuple[int, int]]:
    ids = []

    with open(file, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            id_ranges = line.split(",")
            for id_range in id_ranges:
                bounds = id_range.split("-")
                assert len(bounds) == 2, "expected range had 2 bounds"
                lower = int(bounds[0])
                upper = int(bounds[1])
                ids.append((lower, upper))

    return ids


def _chunks(input, n) -> List[int]:
    chunks = []
    for i in range(0, len(input), n):
        chunks.append(input[i : i + n])
    return chunks


def _all_equal(items: List[Any]) -> bool:
    assert len(items) > 0, "expected not empty list"
    previous = items[0]
    for item in items:
        if item != previous:
            return False
    return True


def sum_invalid_ids_part_1(file: str) -> int:
    invalid = []

    id_ranges = _load_ids(f"{_directory}/{file}")
    for id_range in id_ranges:
        (lower, upper) = id_range
        for i in range(lower, upper + 1):
            number = str(i)
            length = len(number)
            if length % 2 != 0:
                continue
            end_lhs = int((length / 2) - 1)
            start_rhs = end_lhs + 1
            lhs = number[: end_lhs + 1]
            rhs = number[start_rhs:]
            if lhs == rhs:
                invalid.append(i)

    sum = 0
    for value in invalid:
        sum += value

    return sum


def part_1():
    sample = sum_invalid_ids_part_1("p1-sample.input")
    puzzle = sum_invalid_ids_part_1("p1-puzzle.input")
    print("Part 1 - Sample:", sample)
    print("Part 1 - Puzzle:", puzzle)


def sum_invalid_ids_part_2(file: str) -> int:
    invalid = []

    id_ranges = _load_ids(f"{_directory}/{file}")
    for id_range in id_ranges:
        (lower, upper) = id_range
        for i in range(lower, upper + 1):
            number = str(i)
            length = len(number)
            for j in range(1, length):
                if length % j != 0:
                    continue
                items = _chunks(number, j)
                all_equal = _all_equal(items)
                if all_equal:
                    invalid.append(i)
                    break

    sum = 0
    for value in invalid:
        sum += value

    return sum


def part_2():
    sample = sum_invalid_ids_part_2("p1-sample.input")
    puzzle = sum_invalid_ids_part_2("p1-puzzle.input")
    print("Part 2 - Sample:", sample)
    print("Part 2 - Puzzle:", puzzle)


def main():
    part_1()
    part_2()


if __name__ == "__main__":
    main()
