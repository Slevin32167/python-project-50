import pytest
from gendiff import generate_diff

def test_generate_diff_simple():
    """Тест: возвращает строку с путями к файлам."""
    result = generate_diff('tests/fixture/file1.json', 'tests/fixture/file2.json')

    assert result is not None
    assert isinstance(result, str)

    assert 'tests/fixture/file1.json' in result
    assert 'tests/fixture/file2.json' in result


def test_generate_diff_format():
    """Тест: формат вывода."""
    result = generate_diff('tests/fixture/file1.json', 'tests/fixture/file2.json')
    assert len(result) > 0