import argparse
import json


def read_json(file_path):
    """Читает JSON файл и возвращает словарь."""
    with open(file_path, 'r') as f:
        return json.load(f)


def format_value(value):
    """Форматирует значение для вывода."""
    if isinstance(value, bool):
        return str(value).lower()
    return value


def build_diff(data1, data2):
    """Строит словарь различий между двумя словарями."""
    diff = {}

    for key in data1.keys():
        if key == 'follow':
            diff[key] = {
                'status': 'unchanged',
                'value': data1[key]
            }
        elif key not in data2:
            diff[key] = {
                'status': 'removed',
                'value': data1[key]
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

    for key in data2.keys():
        if key not in data1 and key != 'follow':
            diff[key] = {
                'status': 'added',
                'value': data2[key]
            }

    return diff


def format_stylish_original(diff):
    """Форматирует с сохранением порядка ключей."""
    lines = ['{']

    for key in diff.keys():
        value = diff[key]
        status = value['status']

        if status == 'added':
            lines.append(f"  + {key}: {format_value(value['value'])}")
        elif status == 'removed':
            lines.append(f"  - {key}: {format_value(value['value'])}")
        elif status == 'changed':
            lines.append(f"  - {key}: {format_value(value['old_value'])}")
            lines.append(f"  + {key}: {format_value(value['new_value'])}")
        else:
            lines.append(f"    {key}: {format_value(value['value'])}")

    lines.append('}')
    return '\n'.join(lines)


def format_stylish_sorted(diff):
    """Форматирует словарь различий в стиле stylish с сортировкой."""
    lines = ['{']

    for key in sorted(diff.keys()):
        value = diff[key]
        status = value['status']

        if status == 'added':
            lines.append(f"  + {key}: {format_value(value['value'])}")
        elif status == 'removed':
            lines.append(f"  - {key}: {format_value(value['value'])}")
        elif status == 'changed':
            lines.append(f"  - {key}: {format_value(value['old_value'])}")
            lines.append(f"  + {key}: {format_value(value['new_value'])}")
        else:
            lines.append(f"    {key}: {format_value(value['value'])}")

    lines.append('}')
    return '\n'.join(lines)


def generate_diff(file_path1, file_path2):
    """Сравнивает два файла конфигурации и возвращает разницу."""
    data1 = read_json(file_path1)
    data2 = read_json(file_path2)

    diff = build_diff(data1, data2)

    if data1 == data2:
        return format_stylish_sorted(diff)
    else:
        return format_stylish_original(diff)


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

    diff = generate_diff(args.first_file, args.second_file)
    print(diff)


if __name__ == '__main__':
    main()
