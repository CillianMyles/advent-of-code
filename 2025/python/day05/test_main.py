from main import calculate_part_1, calculate_part_2


def test_part_1_sample_input():
    input = "p1-sample.input"
    password = calculate_part_1(input)
    assert password == 3


def test_part_1_puzzle_input():
    input = "p1-puzzle.input"
    password = calculate_part_1(input)
    assert password == -1


def test_part_2_sample_input():
    input = "p1-sample.input"
    password = calculate_part_2(input)
    assert password == 14


def test_part_2_puzzle_input():
    input = "p1-puzzle.input"
    password = calculate_part_2(input)
    assert password == -1
