# Python Functions, Strings and Lists Assessment

## Overview
This repository contains two beginner-friendly Python console programs that
demonstrate **functions**, **string manipulation**, **lists** and **loops**.

| File | Purpose |
|---|---|
| `result_card_generator.py` | Generates a result card for one student |
| `class_marks_analyzer.py` | Analyzes the marks of a whole class |
| `README.md` | Project documentation |

## Program Descriptions

### 1. Result Card Generator (`result_card_generator.py`)
Asks for a student's name, roll number and marks in five subjects, validates
everything, and prints a formatted result card showing marks, total,
percentage (2 decimals), letter grade and Pass/Fail status.

- Roll number must be digits only (`.isdigit()`).
- Each mark must be a whole number from 0 to 100; invalid input is re-asked.
- Name is cleaned with `.strip()` and `.title()`.
- **Rule:** if any subject is below 40, the result is **Fail** regardless of percentage.

Grading table:

| Percentage | Grade |
|---|---|
| 90+ | A+ |
| 80-89 | A |
| 70-79 | B |
| 60-69 | C |
| 50-59 | D |
| Below 50 | Fail |

### 2. Class Marks Analyzer (`class_marks_analyzer.py`)
Asks for the class size, then stores names and marks in two lists
(`student_names`, `student_marks`). It displays:

- Class average
- Highest and lowest marks with the student(s) who got them (ties supported)
- Number of passing (>= 50) and failing (< 50) students
- Students scoring above the class average
- Marks ranked from highest to lowest

## Python Concepts and Functions Used
- **Functions:** `def`, parameters, `return`, `main()` with `if __name__ == "__main__"`
- **Custom functions (Task 1):** `get_valid_marks(subject)`, `calculate_percentage(total, max_total)`, `get_grade(percentage)`, `format_name(name)`, `get_valid_name()`, `get_valid_roll_number()`, `get_final_status()`, `print_result_card()`
- **Custom functions (Task 2):** `get_positive_int()`, `get_valid_mark()`, `find_students_with_mark()`, `count_pass_fail()`
- **Strings:** `.strip()`, `.title()`, `.isdigit()`, `.join()`, f-string formatting (`:.2f`, `:<20`, `:>10`, `:^40`)
- **Lists:** `[]`, `.append()`, `len()`, `sum()`, `max()`, `min()`, `sorted()`, indexing
- **Control flow:** `while True` input loops, `for` loops, `if/elif/else`, `try/except ValueError`
- **Other built-ins:** `zip()`, `enumerate()`, `input()`, `int()`

## How to Run
Requires Python 3.6 or newer.

```bash
git clone https://github.com/<your-username>/python-functions-lists-assessment.git
cd python-functions-lists-assessment

python result_card_generator.py
python class_marks_analyzer.py
```
(Use `python3` instead of `python` on macOS/Linux if needed.)

## Sample Input and Output

### Result Card Generator
```text
--- Student Result Card Generator ---
Enter student name:   ali raza
Enter roll number: abc
  Roll number must contain digits only (e.g. 1024). Try again.
Enter roll number: 1024
Enter marks for English (0-100): 95
Enter marks for Maths (0-100): 150
  Marks must be between 0 and 100.
Enter marks for Maths (0-100): 88
Enter marks for Science (0-100): 92
Enter marks for Computer (0-100): 79
Enter marks for Urdu (0-100): 85

========================================
          STUDENT RESULT CARD
========================================
Name        : Ali Raza
Roll Number : 1024
----------------------------------------
Subject                  Marks
----------------------------------------
English                     95
Maths                       88
Science                     92
Computer                    79
Urdu                        85
----------------------------------------
Total Marks : 439 / 500
Percentage  : 87.80%
Grade       : A
Status      : Pass
========================================
```

**Fail example:** marks of 100, 100, 100, 100, 35 give 87.00%, but because one subject is below 40 the Grade and Status are both **Fail**.

### Class Marks Analyzer
```text
--- Class Marks Analyzer ---
How many students are in the class? 4
Student 1 name: ali
  Enter marks for Ali (0-100): 80
Student 2 name: sara
  Enter marks for Sara (0-100): -5
  Marks must be between 0 and 100.
  Enter marks for Sara (0-100): 95
Student 3 name: bilal
  Enter marks for Bilal (0-100): 40
Student 4 name: hina
  Enter marks for Hina (0-100): 95

========================================
CLASS ANALYSIS
========================================
Class average : 77.50
Highest marks : 95 -> Sara, Hina
Lowest marks  : 40 -> Bilal
Passing (>=50): 3
Failing (<50) : 1

Students above class average:
  Ali - 80
  Sara - 95
  Hina - 95

Marks sorted highest to lowest:
  1. Sara            95
  2. Hina            95
  3. Ali             80
  4. Bilal           40
```

## Author
Your Name - Individual Assessment Submission
