test:
	pytest

test-coverage:
	pytest --cov=src/kata --cov=src/writer --cov-fail-under=90 tests/

type-hint:
	mypy src/main.py src/kata src/writer

run-example:
	python3 src/main.py --folder_path $$(pwd)/examples

run-example-with-incorrect-answer:
	echo "question1.txt" > incorrect_answers.txt
	python3 src/main.py --folder_path $$(pwd)/examples --question_option "incorrect_ans"
	rm incorrect_answers.txt

install-precommit-hook:
	pre-commit install