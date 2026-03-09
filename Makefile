TEST ?=

.PHONY: sync test test-perf test-all clean

sync:
	uv sync

test:
	uv run pytest -vvv -m "not perf" $(TEST)

test-perf:
	uv run pytest -vvv -m perf $(TEST)

test-all:
	uv run pytest -vvv $(TEST)

clean:
	rm -rf .venv .pytest_cache
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
