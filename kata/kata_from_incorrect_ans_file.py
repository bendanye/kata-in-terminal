from os import listdir
from os.path import isfile, join

from kata.kata_from_file import KataFromFile


class KataFromIncorrectAnsFile(KataFromFile):

    def __init__(self, folder_path, questions_folder_name="questions", solutions_folder_name="solutions", incorrect_answers="incorrect_answers.txt"):
        super().__init__(folder_path, questions_folder_name,
                         solutions_folder_name, incorrect_answers)

    def _determine_list_of_questions(self):
        with open(self.incorrect_answers)as file:
            array = file.read().split("\n")
            if array[-1] == "":
                del array[-1]
            return array
