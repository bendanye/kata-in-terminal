import pytest

from src.kata.question_option.invalid_question_option_error import (
    InvalidQuestionOptionError,
)
from src.kata.question_option.question_option_factory import QuestionOptionFactory


def test_should_get_all_questions():
    question_option = QuestionOptionFactory.get_question_option("all", "")
    assert (
        str(type(question_option))
        == "<class 'src.kata.question_option.question_option_all_questions.QuestionOptionAllQuestions'>"
    )


def test_should_get_exception_when_type_not_found():
    with pytest.raises(InvalidQuestionOptionError):
        QuestionOptionFactory.get_question_option("invalid", "")
