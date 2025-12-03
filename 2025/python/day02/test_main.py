from main import sum_invalid_ids_part_1, sum_invalid_ids_part_2


def test_part_1_sample_input():
    input = "p1-sample.input"
    password = sum_invalid_ids_part_1(input)
    assert password == 1227775554


def test_part_1_puzzle_input():
    input = "p1-puzzle.input"
    password = sum_invalid_ids_part_1(input)
    assert password == 19386344315


def test_part_2_sample_input():
    input = "p1-sample.input"
    password = sum_invalid_ids_part_2(input)
    assert password == 4174379265


def test_part_2_puzzle_input():
    input = "p1-puzzle.input"
    password = sum_invalid_ids_part_2(input)
    assert password == 34421651192
