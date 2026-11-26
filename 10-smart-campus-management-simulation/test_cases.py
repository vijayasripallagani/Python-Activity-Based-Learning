"""Test cases for Case Study 10."""
import solution

checks = []


def check(label, actual, expected):
    ok = actual == expected
    checks.append(ok)
    print(("PASS: " if ok else "FAIL: ") + label)


students = []
check("student A1 added", solution.add_student(students, "A1", "Ananya", "CSE"), True)
check("duplicate roll rejected", solution.add_student(students, "A1", "Other", "CSE"), False)
check("empty roll rejected", solution.add_student(students, "", "None", "CSE"), False)

attendance = []
check("18/20 is recorded", solution.record_attendance(attendance, students, "A1", 18, 20), True)
check("eligibility at 90 percent", solution.attendance_eligible(attendance, "A1"), True)
attendance.append(["A2", 13, 20])
check("eligibility at 65 percent", solution.attendance_eligible(attendance, "A2"), False)
check("present greater than total rejected",
      solution.record_attendance(attendance, students, "A1", 25, 20), False)

marks = []
check("marks recorded", solution.record_marks(marks, students, "A1", [85, 78, 90, 82]), True)
check("average gives FIRST grade", solution.grade_for([85, 78, 90, 82]), "FIRST")
check("average gives SECOND grade", solution.grade_for([70, 60, 65, 55]), "SECOND")
check("mark above 100 rejected",
      solution.record_marks(marks, students, "A1", [120, 80]), False)

events = []
check("TechFest registered", solution.register_event(events, students, "A1", "TechFest"), True)
check("duplicate event rejected",
      solution.register_event(events, students, "A1", "TechFest"), False)
check("unknown event rejected",
      solution.register_event(events, students, "A1", "Concert"), False)

routes = [("R1", 180, 40), ("R2", 60, 30)]
plan = solution.allocate_transport(routes)
check("R1 needs 4 buses", plan[0][1], 4)
check("R1 serves 160", plan[0][2], 160)
check("R1 leaves 20 unserved", plan[0][3], 20)
check("R2 needs 2 buses", plan[1][1], 2)
check("R2 has no unserved passengers", plan[1][3], 0)

print("\n%d/%d tests passed." % (sum(checks), len(checks)))
