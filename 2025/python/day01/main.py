from pathlib import Path


_directory = Path(__file__).parent


def determine_password(file: str, start: int = 50) -> int:
    position = start
    zero_count = 0

    with open(f"{_directory}/{file}", "r", encoding="utf-8") as file:
        for line in file:
            instruction = line.strip()
            direction = instruction[0:1]
            distance = int(instruction[1:])

            if direction == "L":
                position = position - distance
                while position < 0:
                    position = position + 100

            elif direction == "R":
                position = position + distance
                while position > 99:
                    position = position - 100

            else:
                raise Exception(f"unexpected direction: {direction}")

            if position == 0:
                zero_count = zero_count + 1

            print(
                f"{instruction} - {direction} - {distance} - {position} - {zero_count}"
            )

    return zero_count


def main():
    determine_password("p1-sample.input")
    determine_password("p1-puzzle.input")


if __name__ == "__main__":
    main()
