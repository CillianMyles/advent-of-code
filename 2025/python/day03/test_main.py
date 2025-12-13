from main import calculate_part_1, calculate_part_2


def test_part_1_sample_input():
    input = "p1-sample.input"
    result = calculate_part_1(input)
    assert result == 357


def test_part_1_puzzle_input():
    input = "p1-puzzle.input"
    result = calculate_part_1(input)
    assert result == 17074


def test_part_2_sample_input():
    input = "p1-sample.input"
    result = calculate_part_2(input)
    assert result == 3121910778619


def test_part_2_puzzle_input():
    input = "p1-puzzle.input"
    result = calculate_part_2(input)
    assert result == 169512729575727
