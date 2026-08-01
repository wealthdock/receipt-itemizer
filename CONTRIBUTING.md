# Contributing to receipt-itemizer

Thanks for your interest in contributing.

## Setup

```bash
uv sync --all-extras
pre-commit install
```

## Before opening a PR

- `uv run ruff check . && uv run ruff format --check .`
- `uv run mypy src tests`
- `uv run pytest`

## Pull requests

Keep PRs focused on a single change. Fill out the PR template and link any related issue.
