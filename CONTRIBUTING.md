<!-- @format -->

# Contributing Guide

Thanks for helping improve the Relational Analysis Vault tooling! This guide explains
how to set up your environment, run checks, and propose changes.

## Prerequisites

- Python 3.12+
- [Node.js](https://nodejs.org/) 18+ (provides `npx` for Markdown tooling)
- [direnv](https://direnv.net/) (optional, but recommended)
- [ruff](https://docs.astral.sh/ruff/) (installed via `pip install ruff` or the
  Makefile/Taskfile)

## Initial Setup

```bash
# Enable direnv (first time only)
direnv allow

# Create a virtual environment and install dependencies
make install
```

The project uses a `.env` file (loaded by direnv) for optional overrides. Copy
`.env.example` to `.env` and update paths as needed.

## Development Workflow

- **Lint**: `make lint` (runs Ruff and markdownlint)
- **Format**: `make format` (Ruff formatter + Prettier + markdownlint fix)
- **Test**: `make test` (pytest suite for vault tooling)
- **All checks**: `make check`

Follow these steps before submitting a pull request.

## Coding Standards

- Python code is linted/formatted with Ruff (see `pyproject.toml` for configuration)
- Markdown follows the conventions documented in `.markdownlintrc`
- Keep docstrings concise; prefer module-level documentation for detailed context

## Git Workflow

1. Create a feature branch
2. Make and test your changes
3. Update relevant documentation (README, schema notes, etc.)
4. Submit a pull request with a clear summary and testing notes

## Testing Tips

Test fixtures live under `tools/vault/test`. You can add new fixtures in
`tools/vault/test/fixtures/` for additional coverage. Run a specific test file with:

```bash
PYTHONPATH=. pytest tools/vault/test/test_vault_loader.py
```

## Filing Issues

When reporting a bug, please include:

- Steps to reproduce
- Expected vs. actual behaviour
- Relevant logs or stack traces
- Python/OS version

Feature requests should include a rationale and any alternative approaches considered.

Thanks again for contributing!
