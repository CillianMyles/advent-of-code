from pathlib import Path
from typing import Iterable, List


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
    total = 0

    num_rows = 0
    row_length = None
    matrix: List[List[str]] = []
    for line in _read_lines(filename):
        row = list(line)
        if row_length is None:
            row_length = len(row)
        else:
            assert row_length == len(row), "unexpected row length"
        matrix.append(row)
        num_rows += 1
        print(f"line: {line} - row: {row} - len: {row_length}")
    assert num_rows, "should be a non-zero number of rows"
    assert row_length, "rows should have a non-zero length"

    range_x = range(row_length - 1)
    range_y = range(num_rows - 1)
    for y in range(num_rows):
        for x in range(row_length):
            adjascent = 0

            top_middle = (x, y - 1)
            top_right = (x + 1, y - 1)
            centre_right = (x + 1, y)
            bottom_right = (x + 1, y + 1)
            bottom_middle = (x, y + 1)
            bottom_left = (x - 1, x + 1)
            centre_left = (x - 1, y)
            top_left = (x - 1, y - 1)

            if (
                top_middle[0] in range_x
                and top_middle[1] in range_y
                and matrix[top_middle[1]][top_middle[0]] == "@"
            ):
                adjascent += 1
                print(f"[x:{x}, y:{y}] - top_middle: {top_middle}: ✅")
            if (
                top_right[0] in range_x
                and top_right[1] in range_y
                and matrix[top_right[1]][top_right[0]] == "@"
            ):
                adjascent += 1
                print(f"[x:{x}, y:{y}] - top_right: {top_right}: ✅")
            if (
                centre_right[0] in range_x
                and centre_right[1] in range_y
                and matrix[centre_right[1]][centre_right[0]] == "@"
            ):
                adjascent += 1
                print(f"[x:{x}, y:{y}] - centre_right: {centre_right}: ✅")
            if (
                bottom_right[0] in range_x
                and bottom_right[1] in range_y
                and matrix[bottom_right[1]][bottom_right[0]] == "@"
            ):
                adjascent += 1
                print(f"[x:{x}, y:{y}] - bottom_right: {bottom_right}: ✅")
            if (
                bottom_middle[0] in range_x
                and bottom_middle[1] in range_y
                and matrix[bottom_middle[1]][bottom_middle[0]] == "@"
            ):
                adjascent += 1
                print(f"[x:{x}, y:{y}] - bottom_middle: {bottom_middle}: ✅")
            if (
                bottom_left[0] in range_x
                and bottom_left[1] in range_y
                and matrix[bottom_left[1]][bottom_left[0]] == "@"
            ):
                adjascent += 1
                print(f"[x:{x}, y:{y}] - bottom_left: {bottom_left}: ✅")
            if (
                centre_left[0] in range_x
                and centre_left[1] in range_y
                and matrix[centre_left[1]][centre_left[0]] == "@"
            ):
                adjascent += 1
                print(f"[x:{x}, y:{y}] - centre_left: {centre_left}: ✅")
            if (
                top_left[0] in range_x
                and top_left[1] in range_y
                and matrix[top_left[1]][top_left[0]] == "@"
            ):
                adjascent += 1
                print(f"[x:{x}, y:{y}] - top_left: {top_left}: ✅")

            if adjascent < 4:
                total += 1

    return total


def calculate_part_2(filename: str) -> int:
    return 0


def part_1():
    sample = calculate_part_1("p1-sample.input")
    # puzzle = calculate_part_1("p1-puzzle.input")
    print("Part 1 - Sample:", sample)
    # print("Part 1 - Puzzle:", puzzle)


def part_2():
    sample = calculate_part_2("p1-sample.input")
    puzzle = calculate_part_2("p1-puzzle.input")
    print("Part 2 - Sample:", sample)
    print("Part 2 - Puzzle:", puzzle)


def main():
    part_1()
    # part_2()


if __name__ == "__main__":
    main()
