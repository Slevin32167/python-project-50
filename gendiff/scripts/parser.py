"""Модуль для парсинга файлов разных форматов."""

import json
import yaml


def parse_file(file_path):
    if file_path.endswith('.json'):
        extension = '.json'
    elif file_path.endswith('.yml') or file_path.endswith('.yaml'):
        extension = '.yml'
    else:
        raise ValueError(f"Unsupported file format: {file_path}")

    with open(file_path, 'r') as f:
        content = f.read()

    if extension == '.json':
        return json.loads(content)
    else:  # .yml или .yaml
        return yaml.safe_load(content)
