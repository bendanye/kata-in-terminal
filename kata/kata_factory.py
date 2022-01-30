from kata.kata_from_file import KataFromFile
from kata.kata_from_incorrect_ans_file import KataFromIncorrectAnsFile

kata_types = {
    "file": KataFromFile,
    "incorrect_ans_file": KataFromIncorrectAnsFile
}


class KataFactory():

    @staticmethod
    def get_kata(type, folder_path, questions_folder_name, solutions_folder_name):
        return kata_types[type](folder_path, questions_folder_name, solutions_folder_name)
