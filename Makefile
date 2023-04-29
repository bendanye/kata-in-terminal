test:
	pytest

test-coverage:
	pytest --cov=src/kata --cov=src/writer --cov-fail-under=90 tests/

type-hint:
	mypy src/main.py src/kata src/writer

run-example:
	python3 src/main.py --folder_path $$(pwd)/examples

install-precommit-hook:
	pre-commit install