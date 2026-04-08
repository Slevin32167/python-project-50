"""Тесты для вычислителя отличий."""

import os
from gendiff import generate_diff


def read_file(file_path):
    """Читает содержимое файла и возвращает строку."""
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read().rstrip('\n')


def get_fixture_path(filename):
    """Возвращает путь к файлу в папке fixtures."""
    return os.path.join('tests', 'fixtures', filename)


def get_expected_path(filename):
    """Возвращает путь к файлу с ожидаемым результатом."""
    return os.path.join('tests', 'test_data', filename)


def test_generate_diff_flat_json():
    """Тест сравнения плоских JSON файлов (stylish)."""
    result = generate_diff(
        get_fixture_path('file1.json'),
        get_fixture_path('file2.json')
    )
    expected = read_file(get_expected_path('expected_flat.txt'))
    assert result == expected


def test_generate_diff_flat_yml():
    """Тест сравнения плоских YAML файлов (stylish)."""
    result = generate_diff(
        get_fixture_path('file1.yml'),
        get_fixture_path('file2.yml')
    )
    expected = read_file(get_expected_path('expected_flat.txt'))
    assert result == expected


def test_generate_diff_nested_json_stylish():
    """Тест сравнения вложенных JSON файлов (stylish)."""
    result = generate_diff(
        get_fixture_path('file1_nested.json'),
        get_fixture_path('file2_nested.json'),
        'stylish'
    )
    expected = read_file(get_expected_path('expected_nested.txt'))
    assert result == expected


def test_generate_diff_nested_yml_stylish():
    """Тест сравнения вложенных YAML файлов (stylish)."""
    result = generate_diff(
        get_fixture_path('file1_nested.yml'),
        get_fixture_path('file2_nested.yml'),
        'stylish'
    )
    expected = read_file(get_expected_path('expected_nested.txt'))
    assert result == expected


def test_generate_diff_nested_json_plain():
    """Тест сравнения вложенных JSON файлов (plain)."""
    result = generate_diff(
        get_fixture_path('file1_nested.json'),
        get_fixture_path('file2_nested.json'),
        'plain'
    )
    expected = read_file(get_expected_path('expected_plain.txt'))
    assert result == expected


def test_generate_diff_nested_yml_plain():
    """Тест сравнения вложенных YAML файлов (plain)."""
    result = generate_diff(
        get_fixture_path('file1_nested.yml'),
        get_fixture_path('file2_nested.yml'),
        'plain'
    )
    expected = read_file(get_expected_path('expected_plain.txt'))
    assert result == expected


def test_generate_diff_identical_files():
    """Тест сравнения одинаковых файлов."""
    result = generate_diff(
        get_fixture_path('file1.json'),
        get_fixture_path('file1.json')
    )
    expected = read_file(get_expected_path('expected_identical.txt'))
    assert result == expected
