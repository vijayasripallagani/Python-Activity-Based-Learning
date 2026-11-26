"""Test cases for Case Study 8."""
import solution

checks = []


def check(label, actual, expected):
    ok = actual == expected
    checks.append(ok)
    print(("PASS: " if ok else "FAIL: ") + label)


check("matrix has 5 students", len(solution.MARKS), 5)
check("every row has 5 subjects", len(solution.MARKS[0]), 5)
check("Ananya total", solution.row_total(solution.MARKS[0]), 404)
check("Fatima total", solution.row_total(solution.MARKS[4]), 456)
check("Maths average", solution.column_average(solution.MARKS, 0), 72.6)
check("Physics average", solution.column_average(solution.MARKS, 1), 67.6)
check("Physics is weak", solution.weak_subjects(solution.MARKS, solution.SUBJECTS), ["Physics"])
check("top performer", solution.top_student(solution.MARKS, solution.NAMES), "Fatima")
check("only Bharat at risk", solution.at_risk(solution.MARKS, solution.NAMES), ["Bharat"])
check("grade A", solution.grade(90), "A")
check("grade B", solution.grade(75), "B")
check("grade C", solution.grade(60), "C")
check("grade D", solution.grade(40), "D")
check("grade F", solution.grade(39), "F")
marks_ok = True
for row in solution.MARKS:
    for mark in row:
        if mark < 0 or mark > 100:
            marks_ok = False
check("all marks within 0 to 100", marks_ok, True)

print("\n%d/%d tests passed." % (sum(checks), len(checks)))
