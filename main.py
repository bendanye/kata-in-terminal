from kata.kata_helper import get_answer_from_solution
from kata.kata_from_file import KataFromFile
import os
import argparse

parser = argparse.ArgumentParser(description='Kata in Terminal.')
parser.add_argument('--question_folder_name', nargs='?', const="questions",
                    default="questions")
parser.add_argument('--solution_folder_name', nargs='?', const="solutions",
                    default="solutions")
parser.add_argument('folder_path', metavar='P',
                    help='Root Path to the questions and solutions')

args = parser.parse_args()

folder_path = args.folder_path
questions_folder_name = args.question_folder_name
solutions_folder_name = args.solution_folder_name

kata = KataFromFile(folder_path, questions_folder_name, solutions_folder_name)

questions = kata.get_questions()
current_question = 0

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    chosen_question = questions[current_question]
    print("\nQuestion: " + chosen_question["question"])
    answer = input("Type the answer:\n")

    solution = kata.get_solution(chosen_question["file_name"])
    solution_answer = get_answer_from_solution(solution)
    if solution_answer == answer:
        print("Correct Answer! ✅")
    else:
        print(
            f"Incorrect Answer! ❌. Correct answer is:\n {solution_answer}")

    input('-> Press enter to move to next question...\n')

    current_question = current_question + 1
    if len(questions) == current_question:
        print("All questions have been asked...")
        break
