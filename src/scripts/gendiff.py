#!/usr/bin/env python
"""Основной модуль."""

import json
import textwrap

from src.cli import parse_cli_arguments

_OUTPUT_TEMPLATE = """
    {{
    {0}
    }}
"""
_ADDED_VALUE = '  + {0}: {1}'
_REMOVED_VALUE = '  - {0}: {1}'
_PRESENTED_VALUE = '    {0}: {1}'


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


def generate_diff(data1, data2):
    """Сравнение содержимого двух файлов.

    Args:
        data1: содержимое первого файла
        data2:  содержимое второго файла

    Returns:
        разница между файлами в виде строки
    """
    keys = sorted(data1.keys() | data2.keys())
    diff = []
    for key in keys:
        data1_value = str(data1.get(key)).lower()
        data2_value = str(data2.get(key)).lower()

        if key not in data1:
            diff.append(_ADDED_VALUE.format(key, data2_value))
        elif key not in data2:
            diff.append(_REMOVED_VALUE.format(key, data1_value))
        elif data1[key] == data2[key]:
            diff.append(_PRESENTED_VALUE.format(key, data1_value))
        else:
            diff.append(_REMOVED_VALUE.format(key, data1_value))
            diff.append(_ADDED_VALUE.format(key, data2_value))

    return textwrap.dedent(_OUTPUT_TEMPLATE).format('\n'.join(diff))


def main():
    """Главная функция."""
    first_file, second_file = parse_cli_arguments()
    first_data = get_file_data(first_file)
    second_data = get_file_data(second_file)
    print(generate_diff(first_data, second_data))


if __name__ == '__main__':
    main()
