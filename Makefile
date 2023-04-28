test:
	pytest

test-coverage:
	pytest --cov=kata --cov-fail-under=90

type-hint:
	mypy src/main.py src/kata

run-example:
	python3 src/main.py --folder_path $$(pwd)/examples

install-precommit-hook:
	pre-commit install