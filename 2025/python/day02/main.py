from pathlib import Path
from typing import List, Iterable, Tuple


_directory = Path(__file__).parent


def _sum_invalid_ids_part_1(file: str) -> int:
    invalid = []
    sum = 0

    with open(f"{_directory}/{file}", "r", encoding="utf-8") as f:
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
                for i in range(lower, upper):
                    if i % 2 != 0:
                        continue
                    else:
                        number = str(i)
                        length = len(number)
                        end_lhs = int((length / 2) - 1)
                        start_rhs = end_lhs + 1
                        lhs = number[: end_lhs + 1]
                        rhs = number[start_rhs:]
                        print(
                            f"number: {number} - length: {length} - end_lhs: {end_lhs} - start_rhs: {start_rhs} - lhs: {lhs} - rhs: {rhs}"
                        )
                        for j in range(start_rhs):
                            if lhs[j] != rhs[j]:
                                continue
                            invalid.append(i)

    for value in invalid:
        sum += value

    return sum


def part_1():
    sample = _sum_invalid_ids_part_1("p1-sample.input")
    print("Part 1 - Sample:", sample)


def main():
    part_1()


if __name__ == "__main__":
    main()
