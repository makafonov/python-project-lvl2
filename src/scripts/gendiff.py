#!/usr/bin/env python
"""Основной модуль."""

import json

from src.cli import parse_cli_arguments
from src.diff import generate_diff


def get_file_data(file_path):
    """Возвращает содержимое файла.

    Args:
        file_path: путь до файла

    Returns:
        содержимое файла
    """
    with open(file_path) as file_object:
        file_data = json.load(file_object)
    return file_data


def main():
    """Главная функция."""
    first_file, second_file = parse_cli_arguments()
    first_data = get_file_data(first_file)
    second_data = get_file_data(second_file)
    print(generate_diff(first_data, second_data))


if __name__ == '__main__':
    main()
