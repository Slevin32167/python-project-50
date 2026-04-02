"""Тесты для вычислителя отличий."""

from gendiff import generate_diff


def test_generate_diff_flat_json():
    """Тест сравнения плоских JSON файлов."""
    result = generate_diff('tests/fixtures/file1.json', 'tests/fixtures/file2.json')
    
    expected = """{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}"""
    
    assert result == expected


def test_generate_diff_identical_files():
    """Тест сравнения одинаковых файлов."""
    result = generate_diff('tests/fixtures/file1.json', 'tests/fixtures/file1.json')
    
    expected = """{
    follow: false
    host: hexlet.io
    proxy: 123.234.53.22
    timeout: 50
}"""
    
    assert result == expected