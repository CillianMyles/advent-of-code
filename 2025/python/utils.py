from typing import Iterator


def read_lines(filepath: str) -> Iterator[str]:
    with open(filepath, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            yield line
