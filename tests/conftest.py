import pytest
from src.scripts.gendiff import get_file_data


@pytest.fixture
def first_file_data():
    return get_file_data('tests/fixtures/file1.json')


@pytest.fixture
def second_file_data():
    return get_file_data('tests/fixtures/file2.json')


@pytest.fixture
def answer():
    with open('tests/fixtures/answer.txt') as file_object:
        file_data = file_object.readlines()
    return ''.join(file_data)


@pytest.fixture
def answer_null_first():
    with open('tests/fixtures/answer_null_first.txt') as file_object:
        file_data = file_object.readlines()
    return ''.join(file_data)


@pytest.fixture
def answer_null_second():
    with open('tests/fixtures/answer_null_second.txt') as file_object:
        file_data = file_object.readlines()
    return ''.join(file_data)
