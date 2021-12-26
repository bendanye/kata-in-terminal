from kata.kata_helper import get_answer_from_solution


def test_get_answer_from_solution_when_answer_in_solution_is_one_line():
    solution = """my solution
####
my answer
####
"""
    assert get_answer_from_solution(solution) == "my answer"


def test_get_answer_from_solution_when_answer_in_solution_is_multiple_lines():
    solution = """my solution
####
my answer

line 1

line 2
####
"""
    assert get_answer_from_solution(
        solution) == "my answer\n\nline 1\n\nline 2"
