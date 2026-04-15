#!/usr/bin/env python3
"""
Вычислитель отличий между конфигурационными файлами.
"""

import argparse
from gendiff.scripts.parser import parse_file
from gendiff.formatters import format_stylish, format_plain, format_json


def build_diff(data1, data2):
    """
    Рекурсивно строит словарь различий между двумя структурами данных.
    """
    diff = {}
    all_keys = sorted(set(data1.keys()) | set(data2.keys()))

    for key in all_keys:
        if key not in data1:
            diff[key] = {
                'status': 'added',
                'value': data2[key]
            }
        elif key not in data2:
            diff[key] = {
                'status': 'removed',
                'value': data1[key]
            }
        elif (isinstance(data1[key], dict)
                and isinstance(data2[key], dict)):
            diff[key] = {
                'status': 'nested',
                'children': build_diff(data1[key], data2[key])
            }
        elif data1[key] != data2[key]:
            diff[key] = {
                'status': 'changed',
                'old_value': data1[key],
                'new_value': data2[key]
            }
        else:
            diff[key] = {
                'status': 'unchanged',
                'value': data1[key]
            }

    return diff


def generate_diff(file_path1, file_path2, format_name='stylish'):
    """
    Сравнивает два файла конфигурации и возвращает разницу.

    Args:
        file_path1: путь к первому файлу
        file_path2: путь ко второму файлу
        format_name: формат вывода ('stylish', 'plain', 'json')

    Returns:
        str: отформатированная разница
    """
    data1 = parse_file(file_path1)
    data2 = parse_file(file_path2)

    diff = build_diff(data1, data2)

    if format_name == 'stylish':
        return format_stylish(diff)
    elif format_name == 'plain':
        return format_plain(diff)
    elif format_name == 'json':
        return format_json(diff)
    else:
        raise ValueError(f"Unsupported format: {format_name}")


def main():
    """Точка входа для консольной команды."""
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )

    parser.add_argument('first_file', help='path to first file')
    parser.add_argument('second_file', help='path to second file')

    parser.add_argument(
        '-f', '--format',
        help='set format of output',
        default='stylish'
    )

    args = parser.parse_args()

    diff = generate_diff(args.first_file, args.second_file, args.format)
    print(diff)


if __name__ == '__main__':
    main()
