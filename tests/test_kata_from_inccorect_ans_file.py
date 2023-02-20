import os
import tempfile
from os.path import join

from kata.kata_from_incorrect_ans_file import KataFromIncorrectAnsFile


def test_get_questions_should_only_get_list_in_incorrect_answer_file():
    with tempfile.TemporaryDirectory() as tmpdirname:
        expected_file_name = "myfile.txt"
        incorrect_answers_file_path = join(tmpdirname, "incorrect_answers.txt")
        f = open(join(tmpdirname, incorrect_answers_file_path), "a")
        f.write("myfile.txt\n")
        f.close()
        expected_question = "my question"
        questions_folder_name = "questions"
        os.mkdir(join(tmpdirname, questions_folder_name))
        f = open(join(tmpdirname, questions_folder_name, expected_file_name), "a")
        f.write(expected_question)
        f.close()
        f = open(join(tmpdirname, questions_folder_name, "my question2"), "a")
        f.write("not expecting question")
        f.close()

        sut = KataFromIncorrectAnsFile(
            folder_path=tmpdirname,
            questions_folder_name=questions_folder_name,
            incorrect_answers=incorrect_answers_file_path,
        )

        assert sut.get_questions() == [
            {"question": expected_question, "file_name": expected_file_name}
        ]
