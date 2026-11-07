"""Task 1: Student Result Card Generator.

Collects a student's details and marks in five subjects, validates them,
and prints a formatted result card with percentage, grade and status.
"""

SUBJECTS = ["English", "Maths", "Science", "Computer", "Urdu"]
MAX_MARKS_PER_SUBJECT = 100
SUBJECT_PASS_MARK = 40   # any subject below this means automatic Fail


def format_name(name):
    # Clean a name by removing extra spaces and capitalising each word.
    return name.strip().title()


def get_valid_name():
    # Keep asking until the user enters a non-empty name, then clean it.
    while True:
        name = format_name(input("Enter student name: "))
        if name:
            return name
        print("  Name cannot be empty. Try again.")


def get_valid_roll_number():
    # Keep asking until the roll number contains digits only.
    while True:
        roll = input("Enter roll number: ").strip()
        if roll.isdigit():
            return roll
        print("  Roll number must contain digits only (e.g. 1024). Try again.")


def get_valid_marks(subject):
    # Ask for marks in one subject until a number from 0 to 100 is entered.
    while True:
        raw = input(f"Enter marks for {subject} (0-100): ").strip()
        try:
            marks = int(raw)
        except ValueError:
            print("  Invalid input. Please enter a whole number.")
            continue
        if 0 <= marks <= MAX_MARKS_PER_SUBJECT:
            return marks
        print("  Marks must be between 0 and 100.")


def calculate_percentage(total, max_total):
    # Return the percentage of total obtained out of max_total.
    return (total / max_total) * 100


def get_grade(percentage):
    # Convert a percentage into a letter grade using the grading table.
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    return "Fail"


def get_final_status(marks_list, grade):
    # Return Fail if any subject is below 40 or the grade is Fail, else Pass.
    if min(marks_list) < SUBJECT_PASS_MARK or grade == "Fail":
        return "Fail"
    return "Pass"


def print_result_card(name, roll, marks_list, total, max_total, percentage, grade, status):
    # Display the final result card using f-strings.
    line = "=" * 40
    print("\n" + line)
    print(f"{'STUDENT RESULT CARD':^40}")
    print(line)
    print(f"Name        : {name}")
    print(f"Roll Number : {roll}")
    print("-" * 40)
    print(f"{'Subject':<20}{'Marks':>10}")
    print("-" * 40)
    for subject, marks in zip(SUBJECTS, marks_list):
        print(f"{subject:<20}{marks:>10}")
    print("-" * 40)
    print(f"Total Marks : {total} / {max_total}")
    print(f"Percentage  : {percentage:.2f}%")
    print(f"Grade       : {grade}")
    print(f"Status      : {status}")
    print(line)


def main():
    # Run the program: collect input, compute results, show the card.
    print("--- Student Result Card Generator ---")
    name = get_valid_name()
    roll = get_valid_roll_number()

    marks_list = []
    for subject in SUBJECTS:
        marks_list.append(get_valid_marks(subject))

    total = sum(marks_list)
    max_total = len(SUBJECTS) * MAX_MARKS_PER_SUBJECT
    percentage = calculate_percentage(total, max_total)

    grade = get_grade(percentage)
    # A failing subject overrides the overall grade.
    if min(marks_list) < SUBJECT_PASS_MARK:
        grade = "Fail"
    status = get_final_status(marks_list, grade)

    print_result_card(name, roll, marks_list, total, max_total, percentage, grade, status)


if __name__ == "__main__":
    main()
