.PHONY: install lint format test check clean

install:
	python3 -m venv .venv
	. .venv/bin/activate && pip install --upgrade pip
	. .venv/bin/activate && pip install -e .

lint:
	direnv exec . ruff check
	direnv exec . markdownlint-cli2 "**/*.md" "!node_modules"

format:
	direnv exec . ruff format
	direnv exec . prettier --write "**/*.md"
	direnv exec . markdownlint-cli2 --fix "**/*.md" "!node_modules"

test:
	direnv exec . pytest

check: lint test

clean:
	rm -rf .venv .mypy_cache .pytest_cache dist build **/__pycache__
	rm -rf tools/vault/extracted
