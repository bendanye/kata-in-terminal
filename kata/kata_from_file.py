from os import listdir
from os.path import isfile, join

from typing import Dict, List


class KataFromFile:
    def __init__(
        self,
        folder_path: str,
        questions_folder_name="questions",
        solutions_folder_name="solutions",
        incorrect_answers="incorrect_answers.txt",
    ):
        self.questions_path = join(folder_path, questions_folder_name)
        self.solutions_path = join(folder_path, solutions_folder_name)
        self.incorrect_answers = incorrect_answers

    def get_questions(self) -> List[Dict[str, str]]:
        questions = self._determine_list_of_questions()

        return [self._populate_question(question) for question in questions]

    def _determine_list_of_questions(self) -> List[str]:
        return [
            f
            for f in listdir(self.questions_path)
            if isfile(join(self.questions_path, f))
        ]

    def get_solution(self, question_file_name: str) -> str:
        solution_path = join(self.solutions_path, question_file_name)
        with open(solution_path, "r") as file:
            solution = file.read()
            return solution

    def _populate_question(self, question: str) -> Dict[str, str]:
        with open(join(self.questions_path, question), "r") as file:
            return {"question": file.read(), "file_name": question}

    def save_incorrect_answer(self, question: str) -> None:
        with open(join(self.incorrect_answers), "a") as file:
            file.write(question)
            file.write("\n")
