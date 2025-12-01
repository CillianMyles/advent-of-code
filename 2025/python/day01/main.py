from pathlib import Path


_directory = Path(__file__).parent


def main():
    position = 50
    zero_count = 0

    with open(f"{_directory}/sample.input", "r", encoding="utf-8") as file:
        for line in file:
            instruction = line.strip()
            direction = instruction[0:1]
            distance = int(instruction[1:])

            if direction == "L":
                if position - distance < 0:
                    # overflow
                    position = position - distance + 100
                else:
                    # normal
                    position = position - distance

            elif direction == "R":
                if position + distance > 99:
                    # overflow
                    position = position + distance - 100
                else:
                    # normal
                    position = position + distance

            else:
                raise Exception(f"unexpected direction: {direction}")

            if position == 0:
                zero_count = zero_count + 1

            print(
                f"{instruction} - {direction} - {distance} - {position} - {zero_count}"
            )


if __name__ == "__main__":
    main()
