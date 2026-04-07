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
    """Тест сравнения плоских JSON файлов."""
    result = generate_diff(
        get_fixture_path('file1.json'),
        get_fixture_path('file2.json')
    )
    expected = read_file(get_expected_path('expected_flat.txt'))
    assert result == expected


def test_generate_diff_flat_yml():
    """Тест сравнения плоских YAML файлов."""
    result = generate_diff(
        get_fixture_path('file1.yml'),
        get_fixture_path('file2.yml')
    )
    expected = read_file(get_expected_path('expected_flat.txt'))
    assert result == expected


def test_generate_diff_identical_files():
    """Тест сравнения одинаковых файлов."""
    result = generate_diff(
        get_fixture_path('file1.json'),
        get_fixture_path('file1.json')
    )
    expected = read_file(get_expected_path('expected_identical.txt'))
    assert result == expected
