# CLAUDE.md

## Project Overview

A collection of Python tests for learning and exploring Python standard library behaviors.

## Commands

- `make sync` - Install dependencies with uv
- `make test` - Run all tests
- `make test TEST=tests/test_copy.py` - Run specific test file
- `make clean` - Remove generated files (.venv, __pycache__, .pytest_cache)

## Project Structure

- `tests/` - Test files exploring Python behaviors
- `pyproject.toml` - Project configuration (Python >=3.12, pytest >=8.0.0)

## Conventions

- Commit messages use commitizen format (e.g., `feat:`, `fix:`, `build:`, `test:`)
- Tests are written to document and verify Python standard library behaviors
