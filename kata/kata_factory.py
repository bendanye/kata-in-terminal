from kata.invalid_kata_type_error import InvalidKataTypeError
from kata.kata_from_file import KataFromFile
from kata.kata_from_incorrect_ans_file import KataFromIncorrectAnsFile

KATA_TYPES = {"file": KataFromFile, "incorrect_ans_file": KataFromIncorrectAnsFile}


class KataFactory:
    @staticmethod
    def get_kata(
        type: str,
        folder_path: str,
        questions_folder_name: str,
        solutions_folder_name: str,
    ):
        if type not in KATA_TYPES:
            raise InvalidKataTypeError(f"invalid type - {type}")

        return KATA_TYPES[type](
            folder_path, questions_folder_name, solutions_folder_name
        )
