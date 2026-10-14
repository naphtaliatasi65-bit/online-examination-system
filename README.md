# Online Examination System

This beginner-friendly project contains two versions:

1. **Enhanced Python terminal version** — supports multiple students and saves results to `results.csv`.
2. **Web version** — uses HTML, CSS, JavaScript, and Python Flask. It includes a countdown timer and saves submitted results to `web_results.csv`.

## Requirements

- Python 3.9 or newer
- Flask for the web version

## Part A: Run the enhanced terminal version

Open a terminal in this folder and run:

```bash
python cli_exam.py
```

Enter a student's name and answer the questions. You can run the exam for multiple students. Results are appended to `results.csv`.

## Part B: Run the web version

Install Flask:

```bash
python -m pip install flask
```

Start the web server:

```bash
python app.py
```

Then open this address in your browser:

`http://127.0.0.1:5000`

Press `Ctrl+C` in the terminal to stop the server.

## How arrays are used

- `QUESTIONS` is a list of question strings.
- `OPTIONS` is a two-dimensional list, with one list of choices per question.
- `CORRECT_ANSWERS` stores the correct choice index for each question.
- The student's answers are stored in a list and compared by matching indexes.

Python indexes start at `0`, so answer index `0` means the first option.

## Important learning note

This is an educational demo, not a secure production examination platform. The web version's timer runs in the browser and should not be treated as tamper-proof. A real system should validate time limits on the server, protect answer keys, use authentication, and use a database with proper access controls.
