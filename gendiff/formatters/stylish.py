"""Stylish форматер для вывода различий."""

from gendiff.formatters.utils import format_value


def format_stylish(diff, depth=0):
    """Форматирует словарь различий в стиле stylish."""
    indent = '  ' * depth  # 2 пробела на уровень глубины
    lines = ['{']

    for key, value in diff.items():
        status = value['status']
        # Для всех элементов используем одинаковый отступ
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
