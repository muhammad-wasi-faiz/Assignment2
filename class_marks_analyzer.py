"""Task 2: Class Marks Analyzer.

Reads names and marks for a class into two parallel lists and reports
average, highest/lowest scorers, pass/fail counts, above-average students
and a ranked list of marks.
"""

PASS_MARK = 50


def get_positive_int(prompt):
    # Ask until the user enters a whole number greater than zero.
    while True:
        raw = input(prompt).strip()
        if raw.isdigit() and int(raw) > 0:
            return int(raw)
        print("  Please enter a whole number greater than 0.")


def get_valid_mark(student_name):
    # Ask for one student's mark until it is a number from 0 to 100.
    while True:
        raw = input(f"  Enter marks for {student_name} (0-100): ").strip()
        try:
            mark = int(raw)
        except ValueError:
            print("  Invalid input. Please enter a whole number.")
            continue
        if 0 <= mark <= 100:
            return mark
        print("  Marks must be between 0 and 100.")


def find_students_with_mark(names, marks, target):
    # Return every student name whose mark equals target (handles ties).
    matches = []
    for i in range(len(marks)):
        if marks[i] == target:
            matches.append(names[i])
    return matches


def count_pass_fail(marks):
    # Return (passed, failed) counts using the pass mark of 50.
    passed = 0
    for m in marks:
        if m >= PASS_MARK:
            passed += 1
    return passed, len(marks) - passed


def main():
    # Run the program: collect data, then display every analysis.
    print("--- Class Marks Analyzer ---")
    student_names = []
    student_marks = []

    count = get_positive_int("How many students are in the class? ")

    # Collect names and marks into the two lists.
    for i in range(1, count + 1):
        name = input(f"Student {i} name: ").strip().title()
        while not name:
            print("  Name cannot be empty.")
            name = input(f"Student {i} name: ").strip().title()
        student_names.append(name)
        student_marks.append(get_valid_mark(name))

    average = sum(student_marks) / len(student_marks)
    highest = max(student_marks)
    lowest = min(student_marks)
    passed, failed = count_pass_fail(student_marks)

    print("\n" + "=" * 40)
    print("CLASS ANALYSIS")
    print("=" * 40)
    print(f"Class average : {average:.2f}")
    print(f"Highest marks : {highest} -> {', '.join(find_students_with_mark(student_names, student_marks, highest))}")
    print(f"Lowest marks  : {lowest} -> {', '.join(find_students_with_mark(student_names, student_marks, lowest))}")
    print(f"Passing (>=50): {passed}")
    print(f"Failing (<50) : {failed}")

    print("\nStudents above class average:")
    found_any = False
    for i in range(len(student_names)):
        if student_marks[i] > average:
            print(f"  {student_names[i]} - {student_marks[i]}")
            found_any = True
    if not found_any:
        print("  None (all students scored equal to the average).")

    print("\nMarks sorted highest to lowest:")
    # Pair each mark with its name, then sort by mark descending.
    ranked = sorted(zip(student_marks, student_names), reverse=True)
    for position, (mark, name) in enumerate(ranked, start=1):
        print(f"  {position}. {name:<15} {mark}")


if __name__ == "__main__":
    main()
