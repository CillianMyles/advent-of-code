from main import determine_password_part_1, determine_password_part_2


def test_part_1_sample_input():
    input = "p1-sample.input"
    password = determine_password_part_1(input)
    assert password == 3


def test_part_1_puzzle_input():
    input = "p1-puzzle.input"
    password = determine_password_part_1(input)
    assert password == 1066


def test_part_2_sample_input():
    input = "p1-sample.input"
    password = determine_password_part_2(input)
    assert password == 6


def test_part_2_example_1():
    input = "p2-sample.input"
    password = determine_password_part_2(input)
    assert password == 10


def test_part_2_example_2():
    input = "p2-sample.input"
    password = determine_password_part_2(input, 0)
    assert password == 10


def test_part_2_puzzle_input():
    input = "p2-sample.input"
    password = determine_password_part_2(input)
    assert password > 5130
