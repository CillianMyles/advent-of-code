from main import part_1, part_2


def test_part_1_sample_input():
    input = "p1-sample.input"
    result = part_1(input)
    assert result == 4277556


def test_part_1_puzzle_input():
    input = "p1-puzzle.input"
    result = part_1(input)
    assert result == 6757749566978


def test_part_2_sample_input():
    input = "p1-sample.input"
    result = part_2(input)
    assert result == 3263827


def test_part_2_puzzle_input():
    input = "p1-puzzle.input"
    result = part_2(input)
    assert result == 10603075273949
