import textwrap

_OUTPUT_TEMPLATE = """
    {{
    {0}
    }}
"""
_ADDED_VALUE = '  + {0}: {1}'
_REMOVED_VALUE = '  - {0}: {1}'
_PRESENTED_VALUE = '    {0}: {1}'


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
