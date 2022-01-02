from kata.kata_from_file import KataFromFile
import tempfile
import os
from os.path import join


def test_get_questions_should_success():
    with tempfile.TemporaryDirectory() as tmpdirname:
        expected_file_name = "myfile.txt"
        expected_question = "my question"
        questions_folder_name = "questions"
        os.mkdir(join(tmpdirname, questions_folder_name))
        f = open(join(tmpdirname, questions_folder_name, expected_file_name), "a")
        f.write(expected_question)
        f.close()

        sut = KataFromFile(folder_path=tmpdirname,
                           questions_folder_name=questions_folder_name)

        assert sut.get_questions() == [{
            "question": expected_question,
            "file_name": expected_file_name
        }]


def test_get_solution_should_success():
    with tempfile.TemporaryDirectory() as tmpdirname:
        expected_file_name = "myfile.txt"
        expected_solution = "my solution"
        solutions_folder_name = "solutions"
        os.mkdir(join(tmpdirname, solutions_folder_name))
        f = open(join(tmpdirname, solutions_folder_name, expected_file_name), "a")
        f.write(expected_solution)
        f.close()

        sut = KataFromFile(folder_path=tmpdirname,
                           solutions_folder_name=solutions_folder_name)

        assert sut.get_solution(expected_file_name) == expected_solution


def test_save_incorrect_answer_should_success():
    with tempfile.TemporaryDirectory() as tmpdirname:
        expected_file_name = "error.txt"
        sut = KataFromFile(folder_path=tmpdirname,
                           incorrect_answers=join(tmpdirname, expected_file_name))

        sut.save_incorrect_answer("incorrect_answer")

        assert os.path.exists(join(tmpdirname, expected_file_name)) is True
