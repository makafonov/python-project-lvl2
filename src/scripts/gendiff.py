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


def generate_diff(first_file, second_file):
    """Сравнение плоских файлов.

    Args:
        first_file: путь до первого файла
        second_file:  путь до второго файла

    Returns:
        разница между файлами в виде строки
    """
    data1 = get_file_data(first_file)
    data2 = get_file_data(second_file)

    keys = sorted(data1.keys() | data2.keys())
    diff = []
    for key in keys:
        if key not in data1:
            diff.append('  + {0}: {1}'.format(key, data2[key]))
        elif key not in data2:
            diff.append('  - {0}: {1}'.format(key, data1[key]))
        elif data1[key] == data2[key]:
            diff.append('    {0}: {1}'.format(key, data1[key]))
        else:
            diff.append('  - {0}: {1}'.format(key, data1[key]))
            diff.append('  + {0}: {1}'.format(key, data2[key]))

    return textwrap.dedent(_OUTPUT_TEMPLATE).format('\n'.join(diff))


def main():
    """Главная функция."""
    print(generate_diff(*parse_cli_arguments()))


if __name__ == '__main__':
    main()
