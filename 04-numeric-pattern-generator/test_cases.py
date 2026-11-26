"""Test cases for Case Study 4."""
import solution

checks = []


def check(label, actual, expected):
    ok = actual == expected
    checks.append(ok)
    print(("PASS: " if ok else "FAIL: ") + label)


check("diamond size 5 accepted", solution.valid_size("diamond", 5), True)
check("diamond height is 9 rows", len(solution.diamond_lines(5)), 9)
check("centre row of diamond", solution.diamond_lines(5)[4], "1 2 3 4 5")
check("top row of diamond", solution.diamond_lines(5)[0], "    1")
check("even diamond size rejected", solution.valid_size("diamond", 6), False)
check("diamond size 1 rejected", solution.valid_size("diamond", 1), False)
check("pyramid size 4 accepted", solution.valid_size("pyramid", 4), True)
check("pyramid top row", solution.pyramid_lines(4)[0], "   1")
check("pyramid last row", solution.pyramid_lines(4)[3], "1234321")
check("negative size rejected", solution.valid_size("pyramid", -2), False)
check("unknown pattern rejected", solution.valid_size("circle", 5), False)

print("\n%d/%d tests passed." % (sum(checks), len(checks)))
