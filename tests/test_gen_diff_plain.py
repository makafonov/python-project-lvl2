from src.scripts.gendiff import generate_diff


def test_gen_diff(first_file_data, second_file_data, answer):
    assert generate_diff({}, {}) == '\n{\n\n}\n'
    assert generate_diff(first_file_data, second_file_data) == answer


def test_gen_diff_null_first(second_file_data, answer_null_first):
    assert generate_diff({}, second_file_data) == answer_null_first


def test_gen_diff_null_second(first_file_data, answer_null_second):
    assert generate_diff(first_file_data, {}) == answer_null_second
