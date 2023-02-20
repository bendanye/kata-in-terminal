from kata.kata_factory import KataFactory


def test_should_get_kata_file():
    kata = KataFactory.get_kata("file", "path", "questions", "solutions")
    assert str(type(kata)) == "<class 'kata.kata_from_file.KataFromFile'>"


def test_should_get_kata_file():
    kata = KataFactory.get_kata("incorrect_ans_file", "path", "questions", "solutions")
    assert (
        str(type(kata))
        == "<class 'kata.kata_from_incorrect_ans_file.KataFromIncorrectAnsFile'>"
    )
