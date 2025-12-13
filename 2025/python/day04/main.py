from pathlib import Path
from typing import Iterator, List


_directory = Path(__file__).parent


def _read_lines(filename: str) -> Iterator[str]:
    filepath = _directory / filename
    with open(filepath, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            yield line


def _read_data(filename: str) -> List[List[str]]:
    data: List[List[str]] = []

    for line in _read_lines(filename):
        row = list(line)
        data.append(row)

    return data


def _calculate_removable_rolls(
    data: List[List[str]],
    reset_value: str | None = None,
) -> int:
    total = 0

    grid = Grid(data)
    for row in range(grid.num_rows):
        for col in range(grid.num_cols):
            point = Point(row, col)
            if grid.value_at(point) != "@":
                continue

            adjacent_rolls = 0
            if grid.value_at(point.top_middle) == "@":
                adjacent_rolls += 1
            if grid.value_at(point.top_right) == "@":
                adjacent_rolls += 1
            if grid.value_at(point.centre_right) == "@":
                adjacent_rolls += 1
            if grid.value_at(point.bottom_right) == "@":
                adjacent_rolls += 1
            if grid.value_at(point.bottom_middle) == "@":
                adjacent_rolls += 1
            if grid.value_at(point.bottom_left) == "@":
                adjacent_rolls += 1
            if grid.value_at(point.centre_left) == "@":
                adjacent_rolls += 1
            if grid.value_at(point.top_left) == "@":
                adjacent_rolls += 1

            if adjacent_rolls < 4:
                total += 1
                if reset_value:
                    data[point.row][point.col] = "."

    return total


def calculate_part_1(filename: str) -> int:
    data = _read_data(filename)
    return _calculate_removable_rolls(data)


def calculate_part_2(filename: str) -> int:
    data = _read_data(filename)
    removed = 0
    while True:
        removable = _calculate_removable_rolls(data, reset_value=".")
        if removable:
            removed += removable
        else:
            break
    return removed


class Point:
    def __init__(self, row: int, col: int):
        self.row = row
        self.col = col

    @property
    def top_middle(self) -> Point:
        return Point(self.row - 1, self.col)

    @property
    def top_right(self) -> Point:
        return Point(self.row - 1, self.col + 1)

    @property
    def centre_right(self) -> Point:
        return Point(self.row, self.col + 1)

    @property
    def bottom_right(self) -> Point:
        return Point(self.row + 1, self.col + 1)

    @property
    def bottom_middle(self) -> Point:
        return Point(self.row + 1, self.col)

    @property
    def bottom_left(self) -> Point:
        return Point(self.row + 1, self.col - 1)

    @property
    def centre_left(self) -> Point:
        return Point(self.row, self.col - 1)

    @property
    def top_left(self) -> Point:
        return Point(self.row - 1, self.col - 1)

    def __str__(self) -> str:
        return f"Point(row: {self.row}, col: {self.col})"

    def __repr__(self) -> str:
        return f"[r:{self.row}, c:{self.col}]"


class Grid:
    def __init__(self, data: List[List[str]]):
        self._data = data
        self.num_rows = len(data)
        self.num_cols: int | None = None
        for row in data:
            if self.num_cols is None:
                self.num_cols = len(row)
            else:
                assert self.num_cols == len(row), "unexpected row length"
        assert self.num_rows, "expected non-zero number of rows"
        assert self.num_cols, "expected non-zero number of columns"

    def in_bounds(self, point: Point) -> bool:
        valid_row = 0 <= point.row < self.num_rows
        valid_col = 0 <= point.col < self.num_cols
        return valid_row and valid_col

    def value_at(self, point: Point) -> str | None:
        if not self.in_bounds(point):
            return None
        return self._data[point.row][point.col]


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
