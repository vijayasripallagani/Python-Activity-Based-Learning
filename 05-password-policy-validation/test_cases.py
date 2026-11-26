"""Test cases for Case Study 5."""
import solution

checks = []


def check(label, actual, expected):
    ok = actual == expected
    checks.append(ok)
    print(("PASS: " if ok else "FAIL: ") + label)


check("valid password accepted", solution.validate("MyCampus#2026"), [])
check("short password fails length", "length below 8" in solution.validate("Ab1!"), True)
check("missing uppercase", "missing uppercase" in solution.validate("campus#123"), True)
check("missing digit", "missing digit" in solution.validate("Campus#abc"), True)
check("missing special", "missing special character" in solution.validate("Campus1234"), True)
check("prohibited admin found", "prohibited word: admin" in solution.validate("Admin#123"), True)
check("triple repeat found",
      "three identical characters in a row" in solution.validate("Camp#aaa2026"), True)
check("abcabc has no triple repeat",
      "three identical characters in a row" in solution.validate("Abcabc#1"), False)
check("two repeats are allowed",
      "three identical characters in a row" in solution.validate("Book#12aA"), False)
check("several failures together", len(solution.validate("abc")), 4)

print("\n%d/%d tests passed." % (sum(checks), len(checks)))
