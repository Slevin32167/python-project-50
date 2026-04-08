"""Plain форматер для вывода различий в плоском виде."""

from gendiff.formatters.utils import stringify_value


def format_plain(diff, path=''):
    """
    Форматирует словарь различий в плоском виде.

    """
    lines = []

    for key, value in diff.items():
        current_path = f"{path}.{key}" if path else key
        status = value['status']

        if status == 'nested':
            lines.append(format_plain(value['children'], current_path))
        elif status == 'added':
            val = stringify_value(value['value'])
            lines.append(
                f"Property '{current_path}' was added with value: {val}"
            )
        elif status == 'removed':
            lines.append(f"Property '{current_path}' was removed")
        elif status == 'changed':
            old_val = stringify_value(value['old_value'])
            new_val = stringify_value(value['new_value'])
            lines.append(
                f"Property '{current_path}' was updated. "
                f"From {old_val} to {new_val}"
            )

    return '\n'.join(lines)
