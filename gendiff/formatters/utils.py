"""Утилиты для форматирования значений."""


def format_value(value, depth=0):
    """Форматирует значение для вывода."""
    if value is None:
        return 'null'
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


def stringify_value(value):
    """Преобразует значение в строку для plain форматера."""
    if value is None:
        return 'null'
    if isinstance(value, bool):
        return str(value).lower()
    if isinstance(value, dict):
        return '[complex value]'
    if isinstance(value, str):
        return f"'{value}'"
    return str(value)
