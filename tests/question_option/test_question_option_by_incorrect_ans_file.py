import tempfile
from os.path import join

from kata.question_option.question_option_by_incorrect_ans_file import (
    QuestionOptionByIncorrectAnsFile,
)


def test_should_get_same_matches_with_incorrect_answer_file():
    expected_questions = ["myfile.txt", "myfile2.txt"]
    with tempfile.TemporaryDirectory() as tmpdirname:
        incorrect_answers_file_path = join(tmpdirname, "incorrect_answers.txt")
        f = open(join(tmpdirname, incorrect_answers_file_path), "a")
        for file_name in expected_questions:
            f.write(f"{file_name}\n")
        f.close()

        sut = QuestionOptionByIncorrectAnsFile(
            incorrect_answers=incorrect_answers_file_path,
        )

        assert sut.select(expected_questions) == expected_questions


def test_should_exclude_not_found_in_questions():
    expected_questions = ["myfile.txt"]
    incorrect_ans = ["myfile.txt", "myfile2.txt"]
    with tempfile.TemporaryDirectory() as tmpdirname:
        incorrect_answers_file_path = join(tmpdirname, "incorrect_answers.txt")
        f = open(join(tmpdirname, incorrect_answers_file_path), "a")
        for file_name in incorrect_ans:
            f.write(f"{file_name}\n")
        f.close()

        sut = QuestionOptionByIncorrectAnsFile(
            incorrect_answers=incorrect_answers_file_path,
        )

        assert sut.select(expected_questions) == expected_questions
