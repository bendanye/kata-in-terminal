import argparse
import os
import sys
import time
from datetime import datetime

sys.path.insert(0, "../kata-in-terminal")

from src.kata.question_option.question_option_factory import QuestionOptionFactory
from src.kata.kata_helper import get_answer_from_solution
from src.kata.kata_from_file import KataFromFile
from os.path import join


def main() -> None:
    args = _parse_args()

    folder_path = args.folder_path
    questions_folder_name = args.question_folder_name
    solutions_folder_name = args.solution_folder_name
    question_option = args.question_option

    incorrect_answers_file_name = "incorrect_answers.txt"

    kata = KataFromFile(
        folder_path,
        QuestionOptionFactory.get_question_option(
            question_option, join(folder_path, incorrect_answers_file_name)
        ),
        questions_folder_name,
        solutions_folder_name,
        incorrect_answers_file_name=incorrect_answers_file_name,
    )

    if not kata.get_questions():
        raise Exception("There is no question found!")

    input("-> Press any keys to start...\n")

    start_time = time.time()
    _start(kata)
    end_time = time.time()

    kata.save_incorrect_answer()
    kata.save_kata_result(
        current_date=datetime.today(), start_time=start_time, end_time=end_time
    )

    print(f"Time taken: {str(round(end_time - start_time))} seconds")
    print(f"Total Questions: {len(kata.get_questions())}")
    print(f"Total Incorrect Answers: {kata.get_total_incorrect_answer()}")


def _parse_args():
    parser = argparse.ArgumentParser(description="Kata in Terminal.")
    parser.add_argument(
        "--question_folder_name", nargs="?", const="questions", default="questions"
    )
    parser.add_argument(
        "--solution_folder_name", nargs="?", const="solutions", default="solutions"
    )
    parser.add_argument("--question_option", nargs="?", const="all", default="all")
    parser.add_argument(
        "--folder_path", metavar="P", help="Root Path to the questions and solutions"
    )

    return parser.parse_args()


def _start(kata) -> None:
    questions = kata.get_questions()
    current_question = 0

    while True:
        os.system("cls" if os.name == "nt" else "clear")
        chosen_question = questions[current_question]
        print("\nQuestion: " + chosen_question.question)
        answer = input("Type the answer:\n")

        solution = kata.get_solution(chosen_question.id)
        solution_answer = get_answer_from_solution(solution)
        if solution_answer == answer:
            print("Correct Answer! ✅")
        else:
            print(f"Incorrect Answer! ❌. Correct answer is:\n {solution_answer}")
            kata.add_incorrect_answer(chosen_question.id)

        input("-> Press any keys to move to next question...\n")

        current_question = current_question + 1
        if len(questions) == current_question:
            print("All questions have been asked.")
            break


if __name__ == "__main__":
    main()
