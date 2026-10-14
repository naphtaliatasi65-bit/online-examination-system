import csv
import os
from datetime import datetime

QUESTIONS = [
    "What is the capital of Ghana?",
    "What is 5 + 3?",
    "Which programming language is this project written in?",
    "How many elements are in an array with 5 items?",
    "Which data structure commonly lets you access items by index?"
]

OPTIONS = [
    ["Accra", "Kumasi", "Tamale", "Ho"],
    ["6", "7", "8", "9"],
    ["Python", "Java", "C++", "PHP"],
    ["3", "4", "5", "6"],
    ["Array", "Graph", "Tree", "Network"]
]

# Correct answer indexes: 0 = first option, 1 = second option, etc.
CORRECT_ANSWERS = [0, 2, 0, 2, 0]
PASS_MARK = 50
RESULTS_FILE = "results.csv"


def run_exam(student_name):
    student_answers = []

    print("\n===== ONLINE EXAMINATION =====")
    print(f"Student: {student_name}")
    print("Choose 1, 2, 3, or 4 for each question.\n")

    for i in range(len(QUESTIONS)):
        print(f"Question {i + 1}: {QUESTIONS[i]}")
        for j in range(len(OPTIONS[i])):
            print(f"  {j + 1}. {OPTIONS[i][j]}")

        while True:
            answer = input("Your answer (1-4): ").strip()
            if answer in {"1", "2", "3", "4"}:
                student_answers.append(int(answer) - 1)
                break
            print("Invalid input. Please enter 1, 2, 3, or 4.")

    score = 0
    for i in range(len(QUESTIONS)):
        if student_answers[i] == CORRECT_ANSWERS[i]:
            score += 1

    total = len(QUESTIONS)
    percentage = round((score / total) * 100, 2)
    status = "PASS" if percentage >= PASS_MARK else "FAIL"

    print("\n===== EXAMINATION RESULT =====")
    print("Student:", student_name)
    print(f"Score: {score}/{total}")
    print(f"Percentage: {percentage}%")
    print("Status:", status)

    save_result(student_name, score, total, percentage, status)


def save_result(name, score, total, percentage, status):
    file_exists = os.path.exists(RESULTS_FILE)
    with open(RESULTS_FILE, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        if not file_exists or os.path.getsize(RESULTS_FILE) == 0:
            writer.writerow(["date_time", "student_name", "score", "total", "percentage", "status"])
        writer.writerow([
            datetime.now().isoformat(timespec="seconds"),
            name,
            score,
            total,
            percentage,
            status
        ])
    print(f"Result saved to {RESULTS_FILE}.")


def main():
    print("=================================")
    print(" ONLINE EXAMINATION SYSTEM")
    print("=================================")

    while True:
        name = input("\nEnter student's name (or type 'quit' to stop): ").strip()
        if name.lower() == "quit":
            print("Goodbye!")
            break
        if not name:
            print("Name cannot be empty.")
            continue

        run_exam(name)

        again = input("\nWould you like to examine another student? (y/n): ").strip().lower()
        if again != "y":
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()
