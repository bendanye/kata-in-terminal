import pytest

from kata.invalid_kata_type_error import InvalidKataTypeError
from kata.kata_factory import KataFactory


def test_should_get_kata_file():
    kata = KataFactory.get_kata("file", "path", "questions", "solutions")
    assert str(type(kata)) == "<class 'kata.kata_from_file.KataFromFile'>"


def test_should_get_kata_incorrect_ans_file():
    kata = KataFactory.get_kata("incorrect_ans_file", "path", "questions", "solutions")
    assert (
        str(type(kata))
        == "<class 'kata.kata_from_incorrect_ans_file.KataFromIncorrectAnsFile'>"
    )


def test_should_get_exception_when_type_not_found():
    with pytest.raises(InvalidKataTypeError):
        KataFactory.get_kata("invalid", "path", "questions", "solutions")
