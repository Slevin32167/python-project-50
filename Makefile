install:
	uv sync

test:
	uv run pytest

test-coverage:
	uv run pytest --cov=gendiff --cov-report=xml:coverage.xml

lint:
	uv run flake8 gendiff

selfcheck:
	uv check

check: selfcheck lint test

build:
	uv build

.PHONY: install test test-coverage lint selfcheck check build
