import glob
import random
from datetime import date
from os.path import isfile, join
from typing import List, Tuple

from src.kata.question import Question
from src.kata.question_option.question_option import QuestionOption
from src.writer.csv_writer import CsvWriter


class KataFromFile:
    def __init__(
        self,
        folder_path: str,
        question_option: QuestionOption,
        questions_folder_name: str = "questions",
        solutions_folder_name: str = "solutions",
        incorrect_answers_file_name: str = "incorrect_answers.txt",
    ) -> None:
        self._questions_path = join(folder_path, questions_folder_name)
        self._solutions_path = join(folder_path, solutions_folder_name)
        self._incorrect_answers_file = join(folder_path, incorrect_answers_file_name)
        self._question_option = question_option
        self._incorrect_answers = []  # type: List[str]
        self._time_taken_path = join(folder_path, "time_taken.txt")

    def get_questions(self) -> Tuple[Question, ...]:
        questions = self._determine_list_of_questions()
        filter_questions = self._question_option.select(questions)
        random.shuffle(filter_questions)
        return tuple(self._populate_question(question) for question in filter_questions)

    def get_solution(self, question_file_name: str) -> str:
        solution_path = join(self._solutions_path, question_file_name)
        with open(solution_path, "r") as file:
            solution = file.read()
            return solution

    def add_incorrect_answer(self, question: str) -> None:
        self._incorrect_answers.append(question)

    def get_total_incorrect_answer(self) -> int:
        return len(self._incorrect_answers)

    def save_incorrect_answer(self) -> None:
        with open(join(self._incorrect_answers_file), "w") as file:
            for incorrect in self._incorrect_answers:
                file.write(incorrect)
                file.write("\n")

    def save_kata_result(
        self, current_date: date, start_time: float, end_time: float
    ) -> None:
        writer = CsvWriter(
            self._time_taken_path,
            headers=[
                "start_date",
                "total_questions",
                "total_incorrect_answers",
                "time_taken_in_secs",
            ],
        )
        writer.write(
            [
                current_date.strftime("%Y-%m-%d"),
                str(len(self.get_questions())),
                str(self.get_total_incorrect_answer()),
                str(round(end_time - start_time)),
            ]
        )

    def _determine_list_of_questions(self) -> List[str]:
        return [
            f.replace(f"{self._questions_path}/", "")
            for f in glob.iglob(self._questions_path + "**/**", recursive=True)
            if isfile(f)
        ]

    def _populate_question(self, question: str) -> Question:
        with open(join(self._questions_path, question), "r") as file:
            return Question(id=question, question=file.read())
