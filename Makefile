TEST ?=

.PHONY: sync test clean

sync:
	uv sync

test:
	uv run pytest -vvv $(TEST)

clean:
	rm -rf .venv .pytest_cache
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
