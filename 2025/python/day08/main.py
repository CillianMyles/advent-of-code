from __future__ import annotations

import math
from pathlib import Path
from typing import Iterator, List, Tuple

_directory = Path(__file__).parent


def _read_lines(filename: str) -> Iterator[str]:
    filepath = _directory / filename
    with filepath.open("r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if line:
                yield line


def part_1(filename: str) -> int:
    print("=" * 50)
    coordinates: List[Coordinate] = []
    for line in _read_lines(filename):
        coords = line.split(",")
        assert len(coords) == 3, "expected 3 coordinates only"
        coordinates.append(
            Coordinate(
                x=int(coords[0]),
                y=int(coords[1]),
                z=int(coords[2]),
            ),
        )
    for i, coordinate in enumerate(coordinates):
        print(f"[{i}] {coordinate!r}")

    print("=" * 50)
    distances: List[Tuple[float, int, int]] = []
    for i, i_coords in enumerate(coordinates):
        for j, j_coords in enumerate(coordinates):
            if i == j:
                continue
            elif any(i == item[2] and j == item[1] for item in distances):
                continue
            distances.append(
                (i_coords.distance_to(j_coords), i, j),
            )
    distances.sort()
    for distance in distances:
        print(distance)

    print("=" * 50)
    return 0


class Coordinate:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def distance_to(self, other: Coordinate) -> float:
        x = self.x - other.x
        y = self.y - other.y
        z = self.z - other.z

        square = (x * x) + (y * y) + (z * z)
        distance = math.sqrt(square)
        return distance

    def __str__(self):
        return f"Coordinate(x: {self.x}, y: {self.y}, x: {self.z})"

    def __repr__(self):
        return f"(x: {self.x}, y: {self.y}, x: {self.z})"


def part_2(filename: str) -> int:
    return 0


def main() -> None:
    sample_1 = part_1("p1-sample.input")
    print(f"Part 1 - Sample: {sample_1}")
    # puzzle_1 = part_1("p1-puzzle.input")
    # print(f"Part 1 - Puzzle: {puzzle_1}")

    # sample_2 = part_2("p1-sample.input")
    # print(f"Part 2 - Sample: {sample_2}")
    # puzzle_2 = part_2("p1-puzzle.input")
    # print(f"Part 2 - Puzzle: {puzzle_2}")


if __name__ == "__main__":
    main()
