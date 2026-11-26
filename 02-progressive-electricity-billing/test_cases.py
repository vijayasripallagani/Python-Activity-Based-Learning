"""Test cases for Case Study 2."""
import solution

checks = []


def check(label, actual, expected):
    ok = actual == expected
    checks.append(ok)
    print(("PASS: " if ok else "FAIL: ") + label)


check("100 units cost Rs 500", solution.slab_charge(100), 500.0)
check("300 units cost Rs 1900", solution.slab_charge(300), 1900.0)
check("500 units cost Rs 3700", solution.slab_charge(500), 3700.0)
check("550 units cost Rs 4300", solution.slab_charge(550), 4300.0)
check("0 units cost 0", solution.slab_charge(0), 0.0)
check("fixed charge included", solution.compute_bill(100, -1)[4], 560.0)
check("cess is 2 percent", solution.compute_bill(100, -1)[2], 10.0)
check("rebate on decrease", solution.compute_bill(100, 200)[3], 25.0)
check("no rebate on increase", solution.compute_bill(200, 100)[3], 0.0)
check("five months are supplied", len(solution.MONTHS), 5)

print("\n%d/%d tests passed." % (sum(checks), len(checks)))
