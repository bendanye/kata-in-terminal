from src.kata.question_option.invalid_question_option_error import (
    InvalidQuestionOptionError,
)
from src.kata.question_option.question_option import QuestionOption
from src.kata.question_option.question_option_all_questions import (
    QuestionOptionAllQuestions,
)
from src.kata.question_option.question_option_by_incorrect_ans_file import (
    QuestionOptionByIncorrectAnsFile,
)


class QuestionOptionFactory:
    @staticmethod
    def get_question_option(option: str, incorrect_answers: str) -> QuestionOption:
        if option == "all":
            return QuestionOptionAllQuestions()
        elif option == "incorrect_ans":
            return QuestionOptionByIncorrectAnsFile(incorrect_answers)
        else:
            raise InvalidQuestionOptionError(f"invalid option - {option}")
