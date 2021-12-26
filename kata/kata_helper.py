from os import listdir
from os.path import isfile, join


def get_questions(questions_path):
    questions = [f for f in listdir(questions_path)
                 if isfile(join(questions_path, f))]

    return [
        _populate_question(questions_path, question)
        for question in questions
    ]


def _populate_question(questions_path, question):
    with open(join(questions_path, question), 'r') as file:
        return {
            "question": file.read(),
            "file_name": question
        }


def get_answer_from_solution(solution):
    return _find_between(solution, "####", "####").strip()


def _find_between(s, first, last):
    try:
        start = s.index(first) + len(first)
        end = s.index(last, start)
        return s[start:end]
    except ValueError:
        return ""
