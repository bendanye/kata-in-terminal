from os import listdir
from os.path import isfile, join


class KataFromFile():

    def __init__(self, folder_path, questions_folder_name="questions", solutions_folder_name="solutions"):
        self.questions_path = join(folder_path, questions_folder_name)
        self.solutions_path = join(folder_path, solutions_folder_name)

    def get_questions(self):
        questions = [f for f in listdir(self.questions_path)
                     if isfile(join(self.questions_path, f))]

        return [
            self._populate_question(question)
            for question in questions
        ]

    def get_solution(self, question_file_name):
        solution_path = join(self.solutions_path, question_file_name)
        with open(solution_path, 'r') as file:
            solution = file.read()
            return solution

    def _populate_question(self, question):
        with open(join(self.questions_path, question), 'r') as file:
            return {
                "question": file.read(),
                "file_name": question
            }
