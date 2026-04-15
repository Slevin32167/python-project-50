# Вычислитель отличий (Difference Calculator)

[![Python CI](https://github.com/Slevin32167/python-project-50/actions/workflows/ci.yml/badge.svg)](https://github.com/Slevin32167/python-project-50/actions/workflows/ci.yml)
[![hexlet-check](https://github.com/Slevin32167/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/Slevin32167/python-project-50/actions/workflows/hexlet-check.yml)

## Описание

**Difference Calculator** — это утилита командной строки для сравнения двух конфигурационных файлов. Она находит различия в структурах и отображает их в наглядном формате. Проект поддерживает файлы форматов **JSON** и **YAML**, а также умеет рекурсивно обрабатывать вложенные структуры.

## Возможности

*   **Поддержка форматов**: JSON (.json), YAML (.yml, .yaml).
*   **Три формата вывода**:
    *   `stylish` (по умолчанию) — наглядное дерево с символами `+` и `-`.
    *   `plain` — текстовое описание изменений.
    *   `json` — машинно-читаемый вывод для интеграции.
*   **Рекурсивное сравнение** вложенных структур.
*   **CI/CD**: автоматическая проверка кода с помощью GitHub Actions.

## Установка и использование

### Требования

*   Python версии 3.10 или выше.
*   Инструмент `uv` (рекомендуется) или `pip`.

### 1. Клонирование репозитория

```bash
git clone https://github.com/Slevin32167/python-project-50.git
cd python-project-50