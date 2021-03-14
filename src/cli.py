"""Модуль для работы с командной строкой."""

import argparse
import pathlib


def parse_cli_arguments():
    """Обработка аргументов командной строки.

    Returns:
        (путь до первого файла, путь до второго файла)
    """
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument(
        'first_file',
        type=pathlib.Path,
    )
    parser.add_argument(
        'second_file',
        type=pathlib.Path,
    )
    parser.add_argument(
        '-f',
        '--format',
        help='set format of output',
    )
    args = parser.parse_args()

    return args.first_file, args.second_file
