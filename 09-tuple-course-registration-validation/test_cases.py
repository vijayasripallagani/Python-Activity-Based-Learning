"""Test cases for Case Study 9."""
import solution

checks = []


def check(label, actual, expected):
    ok = actual == expected
    checks.append(ok)
    print(("PASS: " if ok else "FAIL: ") + label)


check("R01 is valid", solution.validate(solution.REGISTRATIONS[0]), [])
check("R02 duplicate CS101",
      "duplicate CS101" in solution.validate(solution.REGISTRATIONS[1]), True)
check("R03 missing prerequisite",
      "missing CS101 for CS201" in solution.validate(solution.REGISTRATIONS[2]), True)
check("R04 exclusive pair",
      "PHY101 and PHY102 cannot be together" in solution.validate(solution.REGISTRATIONS[3]), True)
check("R04 exceeds course limit",
      "more than 4 courses" in solution.validate(solution.REGISTRATIONS[3]), True)
check("R04 has no duplicate course",
      "duplicate ENG101" in solution.validate(solution.REGISTRATIONS[3]), False)
check("R05 is valid", solution.validate(solution.REGISTRATIONS[4]), [])
check("R06 missing CS201",
      "missing CS201 for CS301" in solution.validate(solution.REGISTRATIONS[5]), True)
check("outer record is a tuple", isinstance(solution.REGISTRATIONS, tuple), True)
check("inner courses are tuples", isinstance(solution.REGISTRATIONS[0][1], tuple), True)
valid = 0
for record in solution.REGISTRATIONS:
    if len(solution.validate(record)) == 0:
        valid = valid + 1
check("2 valid and 4 invalid", (valid, 6 - valid), (2, 4))

print("\n%d/%d tests passed." % (sum(checks), len(checks)))
