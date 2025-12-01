from pathlib import Path


_directory = Path(__file__).parent


def determine_password_part_1(file: str, start: int = 50) -> int:
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


def part_1():
    determine_password_part_1("p1-sample.input")
    determine_password_part_1("p1-puzzle.input")


def determine_password_part_2(file: str, start: int = 50) -> int:
    position = start
    zero_count = 0

    with open(f"{_directory}/{file}", "r", encoding="utf-8") as file:
        for line in file:
            instruction = line.strip()
            direction = instruction[0:1]
            distance = int(instruction[1:])
            starting_position = position

            if direction == "L":
                position = position - distance
                while position < 0:
                    position = position + 100
                    if starting_position != 0 and position != 0:
                        zero_count = zero_count + 1

            elif direction == "R":
                position = position + distance
                while position > 99:
                    position = position - 100
                    if starting_position != 0 and position != 0:
                        zero_count = zero_count + 1

            else:
                raise Exception(f"unexpected direction: {direction}")

            if position == 0:
                zero_count = zero_count + 1

            print(f"{starting_position} - {instruction} - {position} - {zero_count}")

    return zero_count


def part_2():
    # determine_password_part_2("p2-sample.input", 0)
    # determine_password_part_2("p1-sample.input")
    determine_password_part_2("p1-puzzle.input")


def main():
    # part_1()
    part_2()


if __name__ == "__main__":
    main()
