test:
	pytest

type_hint:
	mypy main.py kata

run_example:
	python3 main.py --folder_path examples