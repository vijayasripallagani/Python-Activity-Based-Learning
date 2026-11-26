"""
Case Study 8: Student Marks Matrix Analysis
Nested lists, loops, tuples and conditional statements.
"""

NAMES = ("Ananya", "Bharat", "Chitra", "Deepak", "Fatima")
SUBJECTS = ("Maths", "Physics", "Chemistry", "English", "Computer")
MARKS = [
    [82, 76, 90, 71, 85],
    [55, 48, 62, 70, 58],
    [74, 69, 71, 66, 80],
    [61, 57, 64, 59, 66],
    [91, 88, 94, 87, 96],
]
WEAK_AVERAGE = 70.0
PASS_MARK = 50


def row_total(row):
    total = 0
    for mark in row:
        total = total + mark
    return total


def row_average(row):
    return row_total(row) / len(row)


def column_average(matrix, column):
    total = 0
    for row in matrix:
        total = total + row[column]
    return total / len(matrix)


def grade(average):
    if average >= 85:
        return "A"
    elif average >= 75:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 40:
        return "D"
    return "F"


def top_student(matrix, names):
    best = 0
    for i in range(1, len(matrix)):
        if row_total(matrix[i]) > row_total(matrix[best]):
            best = i
    return names[best]


def weak_subjects(matrix, subjects):
    weak = []
    for c in range(len(subjects)):
        if column_average(matrix, c) < WEAK_AVERAGE:
            weak.append(subjects[c])
    return weak


def at_risk(matrix, names):
    risk = []
    for i in range(len(matrix)):
        for mark in matrix[i]:
            if mark < PASS_MARK:
                risk.append(names[i])
                break
    return risk


def main():
    print("=" * 74)
    print("STUDENT MARKS MATRIX ANALYSIS")
    print("=" * 74)
    print("%-9s %6s %9s %6s" % ("Name", "Total", "Average", "Grade"))
    for i in range(len(MARKS)):
        average = row_average(MARKS[i])
        print("%-9s %6d %9.1f %6s" %
              (NAMES[i], row_total(MARKS[i]), average, grade(average)))
    print("\nSUBJECT AVERAGES")
    for c in range(len(SUBJECTS)):
        print("%-10s %.1f" % (SUBJECTS[c], column_average(MARKS, c)))
    print("\nTop performer : " + top_student(MARKS, NAMES))
    print("Weak subjects : " + ", ".join(weak_subjects(MARKS, SUBJECTS)))
    print("At-risk list  : " + ", ".join(at_risk(MARKS, NAMES)))


if __name__ == "__main__":
    main()
