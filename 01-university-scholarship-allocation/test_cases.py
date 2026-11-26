"""Test cases for Case Study 1."""
import solution

checks = []


def check(label, actual, expected):
    ok = actual == expected
    checks.append(ok)
    print(("PASS: " if ok else "FAIL: ") + label)


ok, agg, reasons = solution.evaluate(solution.APPLICANTS[0])
check("S101 is eligible", ok, True)
check("S101 aggregate is 80.8", agg, 80.8)
ok, agg, reasons = solution.evaluate(solution.APPLICANTS[1])
check("S102 is rejected", ok, False)
check("S102 has two reasons", len(reasons), 2)
ok, agg, reasons = solution.evaluate(solution.APPLICANTS[2])
check("S103 rejected on income", "income above limit" in reasons, True)
ok, agg, reasons = solution.evaluate(solution.APPLICANTS[5])
check("S106 rejected on attendance", "attendance below 75" in reasons, True)
check("S105 has the best aggregate", solution.rank_applicants([
    ("S104", "Deepak", 61.4, 76, 495000),
    ("S105", "Fatima", 91.2, 97, 250000),
])[0][0], "S105")
check("tie broken by attendance", solution.rank_applicants([
    ("S104", "Deepak", 61.4, 76, 495000),
    ("S108", "Ishaan", 61.4, 88, 410000),
])[0][0], "S108")

eligible_count = 0
for applicant in solution.APPLICANTS:
    ok, agg, reasons = solution.evaluate(applicant)
    if ok:
        eligible_count = eligible_count + 1
check("4 eligible applicants", eligible_count, 4)
check("4 rejected applicants", len(solution.APPLICANTS) - eligible_count, 4)

print("\n%d/%d tests passed." % (sum(checks), len(checks)))
