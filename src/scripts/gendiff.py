#!/usr/bin/env python
import argparse
import pathlib

parser = argparse.ArgumentParser(description='Generate diff')
parser.add_argument(
    'first_file',
    type=pathlib.Path,
)
parser.add_argument(
    'second_file',
    type=pathlib.Path,
)

args = parser.parse_args()
