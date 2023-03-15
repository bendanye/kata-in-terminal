test:
	pytest

test_coverage:
	pytest --cov=kata --cov-fail-under=90

type_hint:
	mypy main.py kata

run_example:
	python3 main.py --folder_path examples

install_precommit_hook:
	pre-commit install