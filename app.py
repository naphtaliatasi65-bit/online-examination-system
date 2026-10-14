from datetime import datetime
import csv
import os
from flask import Flask, render_template, request

app = Flask(__name__)

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

CORRECT_ANSWERS = [0, 2, 0, 2, 0]
PASS_MARK = 50
TIME_LIMIT_SECONDS = 120
RESULTS_FILE = "web_results.csv"


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


@app.route("/", methods=["GET", "POST"])
def exam():
    if request.method == "POST":
        name = request.form.get("student_name", "").strip()
        if not name:
            return render_template(
                "exam.html",
                questions=QUESTIONS,
                options=OPTIONS,
                time_limit=TIME_LIMIT_SECONDS,
                error="Please enter your name."
            )

        answers = []
        for i in range(len(QUESTIONS)):
            raw_answer = request.form.get(f"q{i}")
            try:
                answer = int(raw_answer)
            except (TypeError, ValueError):
                answer = -1
            answers.append(answer)

        score = 0
        for i in range(len(QUESTIONS)):
            if answers[i] == CORRECT_ANSWERS[i]:
                score += 1

        total = len(QUESTIONS)
        percentage = round((score / total) * 100, 2)
        status = "PASS" if percentage >= PASS_MARK else "FAIL"
        save_result(name, score, total, percentage, status)

        return render_template(
            "result.html",
            name=name,
            score=score,
            total=total,
            percentage=percentage,
            status=status,
            questions=QUESTIONS,
            options=OPTIONS,
            answers=answers,
            correct_answers=CORRECT_ANSWERS
        )

    return render_template(
        "exam.html",
        questions=QUESTIONS,
        options=OPTIONS,
        time_limit=TIME_LIMIT_SECONDS,
        error=None
    )


if __name__ == "__main__":
    # Debug mode is convenient for learning. Do not use it on a public production server.
    app.run(debug=True)
