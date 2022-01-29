from kata.kata_from_file import KataFromFile


class KataFactory():

    @staticmethod
    def get_kata(type, folder_path, questions_folder_name, solutions_folder_name):
        return KataFromFile(folder_path, questions_folder_name, solutions_folder_name)
