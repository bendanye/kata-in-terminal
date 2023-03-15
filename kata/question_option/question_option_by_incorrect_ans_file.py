from typing import List


class QuestionOptionByIncorrectAnsFile:
    def __init__(
        self,
        incorrect_answers: str = "incorrect_answers.txt",
    ) -> None:
        self._incorrect_answers = incorrect_answers

    def select(self, questions: List[str]) -> List[str]:
        incorrect_answers = self._get_incorrect_answers()
        return [
            incorrect_answer
            for incorrect_answer in incorrect_answers
            if incorrect_answer in questions
        ]

    def _get_incorrect_answers(self) -> List[str]:
        with open(self._incorrect_answers) as file:
            array = file.read().split("\n")
            if array[-1] == "":
                del array[-1]
            return array
