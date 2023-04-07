test:
	pytest

test-coverage:
	pytest --cov=kata --cov-fail-under=90

type-hint:
	mypy main.py kata

run-example:
	python3 main.py --folder_path examples

install-precommit-hook:
	pre-commit install