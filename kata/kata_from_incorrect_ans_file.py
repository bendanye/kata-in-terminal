from typing import List

from kata.kata_from_file import KataFromFile


class KataFromIncorrectAnsFile(KataFromFile):
    def __init__(
        self,
        folder_path: str,
        questions_folder_name: str = "questions",
        solutions_folder_name: str = "solutions",
        incorrect_answers: str = "incorrect_answers.txt",
    ) -> None:
        super().__init__(
            folder_path, questions_folder_name, solutions_folder_name, incorrect_answers
        )

    def _determine_list_of_questions(self) -> List[str]:
        with open(self._incorrect_answers) as file:
            array = file.read().split("\n")
            if array[-1] == "":
                del array[-1]
            return array
