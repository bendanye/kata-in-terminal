import glob
import random
from os.path import isfile, join
from typing import List, Tuple

from kata.question import Question


class KataFromFile:
    def __init__(
        self,
        folder_path: str,
        questions_folder_name: str = "questions",
        solutions_folder_name: str = "solutions",
        incorrect_answers: str = "incorrect_answers.txt",
    ) -> None:
        self._questions_path = join(folder_path, questions_folder_name)
        self._solutions_path = join(folder_path, solutions_folder_name)
        self._incorrect_answers = incorrect_answers

    def get_questions(self) -> Tuple[Question, ...]:
        questions = self._determine_list_of_questions()

        random.shuffle(questions)

        return tuple(self._populate_question(question) for question in questions)

    def _determine_list_of_questions(self) -> List[str]:
        return [
            f.replace(f"{self._questions_path}/", "")
            for f in glob.iglob(self._questions_path + "**/**", recursive=True)
            if isfile(f)
        ]

    def get_solution(self, question_file_name: str) -> str:
        solution_path = join(self._solutions_path, question_file_name)
        with open(solution_path, "r") as file:
            solution = file.read()
            return solution

    def _populate_question(self, question: str) -> Question:
        with open(join(self._questions_path, question), "r") as file:
            return Question(id=question, question=file.read())

    def save_incorrect_answer(self, question: str) -> None:
        with open(join(self._incorrect_answers), "a") as file:
            file.write(question)
            file.write("\n")
