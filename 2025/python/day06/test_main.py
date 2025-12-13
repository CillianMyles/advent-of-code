from main import calculate_part_1, calculate_part_2


def test_part_1_sample_input():
    input = "p1-sample.input"
    result = calculate_part_1(input)
    assert result == 4277556


def test_part_1_puzzle_input():
    input = "p1-puzzle.input"
    result = calculate_part_1(input)
    assert result == 6757749566978


def test_part_2_sample_input():
    input = "p1-sample.input"
    result = calculate_part_2(input)
    assert result == -1


def test_part_2_puzzle_input():
    input = "p1-puzzle.input"
    result = calculate_part_2(input)
    assert result == -1
