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
    num_columns = None
    matrix: List[List[str]] = []
    for line in _read_lines(filename):
        row = list(line)
        if num_columns is None:
            num_columns = len(row)
        else:
            assert num_columns == len(row), "unexpected row length"
        matrix.append(row)
        num_rows += 1
        print(f"line: {line} - row: {row} - len: {num_columns}")
    assert num_rows, "should be a non-zero number of rows"
    assert num_columns, "should be a non-zero number of columns"

    max_x = num_columns
    max_y = num_rows

    def in_bounds(x, y):
        return 0 <= x < max_x and 0 <= y < max_y

    for y in range(num_rows):
        for x in range(num_columns):
            adjascent = 0

            top_middle = (x, y - 1)
            top_right = (x + 1, y - 1)
            centre_right = (x + 1, y)
            bottom_right = (x + 1, y + 1)
            bottom_middle = (x, y + 1)
            bottom_left = (x - 1, y + 1)
            centre_left = (x - 1, y)
            top_left = (x - 1, y - 1)

            if (
                in_bounds(*top_middle)
                and matrix[top_middle[1]][top_middle[0]] == "@"
            ):
                adjascent += 1
                print(f"[x:{x}, y:{y}] - top_middle: {top_middle}: ✅")
            if (
                in_bounds(*top_right)
                and matrix[top_right[1]][top_right[0]] == "@"
            ):
                adjascent += 1
                print(f"[x:{x}, y:{y}] - top_right: {top_right}: ✅")
            if (
                in_bounds(*centre_right)
                and matrix[centre_right[1]][centre_right[0]] == "@"
            ):
                adjascent += 1
                print(f"[x:{x}, y:{y}] - centre_right: {centre_right}: ✅")
            if (
                in_bounds(*bottom_right)
                and matrix[bottom_right[1]][bottom_right[0]] == "@"
            ):
                adjascent += 1
                print(f"[x:{x}, y:{y}] - bottom_right: {bottom_right}: ✅")
            if (
                in_bounds(*bottom_middle)
                and matrix[bottom_middle[1]][bottom_middle[0]] == "@"
            ):
                adjascent += 1
                print(f"[x:{x}, y:{y}] - bottom_middle: {bottom_middle}: ✅")
            if (
                in_bounds(*bottom_left)
                and matrix[bottom_left[1]][bottom_left[0]] == "@"
            ):
                adjascent += 1
                print(f"[x:{x}, y:{y}] - bottom_left: {bottom_left}: ✅")
            if (
                in_bounds(*centre_left)
                and matrix[centre_left[1]][centre_left[0]] == "@"
            ):
                adjascent += 1
                print(f"[x:{x}, y:{y}] - centre_left: {centre_left}: ✅")
            if (
                in_bounds(*top_left)
                and matrix[top_left[1]][top_left[0]] == "@"
            ):
                adjascent += 1
                print(f"[x:{x}, y:{y}] - top_left: {top_left}: ✅")

            if adjascent < 4:
                total += 1

    return total


def calculate_part_2(filename: str) -> int:
    return 0


class Point:
    def __init__(self, row: int, column: int):
        self._row = row
        self._column = column

    def r(self) -> int:
        return self._row

    def c(self) -> int:
        return self._column

    def top_middle(self):
        return Point(self.r - 1, self.c)

    def top_right(self):
        return Point(self.r - 1, self.c + 1)

    def centre_right(self):
        return Point(self.r, self.c + 1)

    def bottom_right(self):
        return Point(self.r + 1, self.c + 1)

    def bottom_middle(self):
        return Point(self.r + 1, self.c)

    def bottom_left(self):
        return Point(self.r + 1, self.c - 1)

    def centre_left(self):
        return Point(self.r, self.c - 1)

    def top_left(self):
        return Point(self.r - 1, self.c - 1)

    def __str__(self):
        return f"Point(row: {self.r}, column: {self.c})"


class Grid:
    def __init__(self, data: List[List[str]]):
        self._data = data
        self._num_rows = len(data)
        self._num_cols: int | None = None
        for row in data:
            for column in row:
                if self._num_cols is None:
                    self._num_cols = len(column)
                else:
                    assert self._num_cols == len(column)

    def in_bounds(self, point: Point) -> bool:
        return 0 <= point.r < self._num_rows and 0 <= point.c < self._num_cols

    def value_at(self, point: Point) -> str | None:
        if not self.in_bounds(point):
            return None
        return self._data[point.c][point.r]


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
