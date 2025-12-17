from main import part_1, part_2


def test_part_1_sample_input():
    input = "p1-sample.input"
    result = part_1(input)
    assert result == 21


def test_part_1_puzzle_input():
    input = "p1-puzzle.input"
    result = part_1(input)
    assert result == -1


def test_part_2_sample_input():
    input = "p1-sample.input"
    result = part_2(input)
    assert result == -1


def test_part_2_puzzle_input():
    input = "p1-puzzle.input"
    result = part_2(input)
    assert result == -1
