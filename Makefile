SHELL := /bin/bash

.PHONY: install lint format test check clean

RUN = if command -v direnv >/dev/null 2>&1; then \
	direnv exec . $(1); \
elif [ -f .venv/bin/activate ]; then \
	source .venv/bin/activate && $(1); \
else \
	$(1); \
fi

install:
	python3 -m venv .venv
	. .venv/bin/activate && pip install --upgrade pip
	. .venv/bin/activate && pip install -e .

lint:
	@$(call RUN,ruff check)
	@$(call RUN,npx --yes markdownlint-cli2 --config .markdownlint-cli2.yaml "**/*.md" "!node_modules")

format:
	@$(call RUN,ruff format)
	@$(call RUN,npx --yes prettier --write "**/*.md")
	@$(call RUN,npx --yes markdownlint-cli2 --config .markdownlint-cli2.yaml --fix "**/*.md" "!node_modules")

test:
	@$(call RUN,pytest)

check: lint test

clean:
	rm -rf .venv .mypy_cache .pytest_cache dist build
	find . -name '__pycache__' -type d -prune -exec rm -rf {} +
	rm -rf tools/vault/extracted
