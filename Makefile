install:
	uv sync

test:
	uv run pytest

test-coverage:
	uv run pytest --cov=gendiff --cov-report=xml:coverage.xml

lint:
	uv run ruff check gendiff

check: lint test

build:
	uv build

.PHONY: install test test-coverage lint check build
