"""
Вычислитель отличий между конфигурационными файлами.
"""

import argparse
from gendiff.parser import parse_file


def format_value(value, depth=0):
    """Форматирует значение для вывода с учетом глубины."""
    if isinstance(value, bool):
        return str(value).lower()
    if isinstance(value, dict):
        indent = '    ' * depth
        lines = ['{']
        for k, v in value.items():
            lines.append(
                f"{indent}    {k}: {format_value(v, depth + 1)}"
            )
        lines.append(f"{indent}}}")
        return '\n'.join(lines)
    return value


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


def format_stylish(diff, depth=0):
    """Форматирует словарь различий в стиле stylish."""
    indent = '    ' * depth
    lines = ['{']

    for key, value in diff.items():
        status = value['status']
        current_indent = indent + '  '

        if status == 'nested':
            children = format_stylish(value['children'], depth + 1)
            lines.append(f"{current_indent}{key}: {children}")
        elif status == 'added':
            val = format_value(value['value'], depth + 1)
            lines.append(f"{current_indent}+ {key}: {val}")
        elif status == 'removed':
            val = format_value(value['value'], depth + 1)
            lines.append(f"{current_indent}- {key}: {val}")
        elif status == 'changed':
            old_val = format_value(value['old_value'], depth + 1)
            new_val = format_value(value['new_value'], depth + 1)
            lines.append(f"{current_indent}- {key}: {old_val}")
            lines.append(f"{current_indent}+ {key}: {new_val}")
        else:  # unchanged
            val = format_value(value['value'], depth + 1)
            lines.append(f"{current_indent}  {key}: {val}")

    lines.append(indent + '}')
    return '\n'.join(lines)


def generate_diff(file_path1, file_path2, format_name='stylish'):
    """
    Сравнивает два файла конфигурации и возвращает разницу.
    """
    data1 = parse_file(file_path1)
    data2 = parse_file(file_path2)

    diff = build_diff(data1, data2)

    if format_name == 'stylish':
        return format_stylish(diff)
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
