import os
import tempfile
import datetime

from os.path import join

from src.kata.kata_from_file import KataFromFile
from src.kata.question import Question
from src.kata.question_option.question_option_all_questions import (
    QuestionOptionAllQuestions,
)


def test_get_questions_should_success():
    with tempfile.TemporaryDirectory() as tmp_dir_name:
        questions_folder_name = "questions"
        expected_question = "my question"
        expected_file_name = "myfile.txt"
        os.mkdir(join(tmp_dir_name, questions_folder_name))
        f = open(join(tmp_dir_name, questions_folder_name, expected_file_name), "a")
        f.write(expected_question)
        f.close()

        sut = KataFromFile(
            folder_path=tmp_dir_name,
            question_option=QuestionOptionAllQuestions(),
            questions_folder_name=questions_folder_name,
        )

        assert sut.get_questions() == (
            Question(id=expected_file_name, question=expected_question),
        )


def test_get_questions_in_subdirectory_should_success():
    with tempfile.TemporaryDirectory() as tmp_dir_name:
        questions_folder_name = "questions"
        subfolder_name = "subfolder"
        expected_question = "my question"
        expected_file_name = join(subfolder_name, "myfile.txt")
        os.makedirs(join(tmp_dir_name, questions_folder_name, subfolder_name))
        f = open(join(tmp_dir_name, questions_folder_name, expected_file_name), "a")
        f.write(expected_question)
        f.close()

        sut = KataFromFile(
            folder_path=tmp_dir_name,
            question_option=QuestionOptionAllQuestions(),
            questions_folder_name=questions_folder_name,
        )

        assert sut.get_questions() == (
            Question(id=expected_file_name, question=expected_question),
        )


def test_get_solution_should_success():
    with tempfile.TemporaryDirectory() as tmp_dir_name:
        expected_file_name = "myfile.txt"
        expected_solution = "my solution"
        solutions_folder_name = "solutions"
        os.mkdir(join(tmp_dir_name, solutions_folder_name))
        f = open(join(tmp_dir_name, solutions_folder_name, expected_file_name), "a")
        f.write(expected_solution)
        f.close()

        sut = KataFromFile(
            folder_path=tmp_dir_name,
            question_option=QuestionOptionAllQuestions(),
            solutions_folder_name=solutions_folder_name,
        )

        assert sut.get_solution(expected_file_name) == expected_solution


def test_save_incorrect_answer_should_success():
    with tempfile.TemporaryDirectory() as tmp_dir_name:
        incorrect_answers_file_path = join(tmp_dir_name, "incorrect_answers.txt")
        sut = KataFromFile(
            folder_path=tmp_dir_name,
            question_option=QuestionOptionAllQuestions(),
            incorrect_answers_file_name=incorrect_answers_file_path,
        )

        sut.add_incorrect_answer("incorrect_answer1")
        sut.add_incorrect_answer("incorrect_answer2")

        sut.save_incorrect_answer()

        assert os.path.exists(incorrect_answers_file_path) is True
        with open(incorrect_answers_file_path, "r") as actual_file:
            assert "incorrect_answer1\nincorrect_answer2\n" == actual_file.read()


def test_save_kata_result_should_success():
    with tempfile.TemporaryDirectory() as tmp_dir_name:
        time_taken_file_path = join(tmp_dir_name, "time_taken.txt")
        questions_folder_name = "questions"
        expected_question = "my question"
        expected_file_name = "myfile.txt"
        os.mkdir(join(tmp_dir_name, questions_folder_name))
        f = open(join(tmp_dir_name, questions_folder_name, expected_file_name), "a")
        f.write(expected_question)
        f.close()
        sut = KataFromFile(
            folder_path=tmp_dir_name,
            questions_folder_name=questions_folder_name,
            question_option=QuestionOptionAllQuestions(),
            incorrect_answers_file_name="incorrect_answers_file_path",
        )
        sut.add_incorrect_answer("incorrect1")
        current_date = datetime.date(2023, 1, 2)

        sut.save_kata_result(current_date=current_date, start_time=1, end_time=2)

        assert os.path.exists(time_taken_file_path) is True
        with open(time_taken_file_path, "r") as actual_file:
            assert (
                "start_date,total_questions,total_incorrect_answers,time_taken_in_secs\n2023-01-02,1,1,1\n"
                == actual_file.read()
            )
