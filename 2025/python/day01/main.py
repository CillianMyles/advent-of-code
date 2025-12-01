from pathlib import Path


_directory = Path(__file__).parent


def main():
    with open(f"{_directory}/sample.input", "r", encoding="utf-8") as file:
        for line in file:
            print(line.strip())


if __name__ == "__main__":
    main()
