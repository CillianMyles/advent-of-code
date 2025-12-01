from main import determine_password_part_1


def test_part_1_sample_input():
    input = "p1-sample.input"
    password = determine_password_part_1(input)
    assert password == 3


def test_part_1_puzzle_input():
    input = "p1-puzzle.input"
    password = determine_password_part_1(input)
    assert password == 1066
