"""Test cases for Case Study 7."""
import solution

checks = []


def check(label, actual, expected):
    ok = actual == expected
    checks.append(ok)
    print(("PASS: " if ok else "FAIL: ") + label)


log = []
balance, message = solution.deposit(5000.0, 1500.0, log)
check("deposit accepted", balance, 6500.0)
check("deposit is logged", len(log), 1)
balance, message = solution.deposit(5000.0, -10.0, [])
check("negative deposit rejected", balance, 5000.0)
balance, message = solution.deposit(5000.0, 100001.0, [])
check("large deposit rejected", balance, 5000.0)
balance, message = solution.withdraw(5000.0, 2000.0, log)
check("valid withdrawal", balance, 3000.0)
balance, message = solution.withdraw(5000.0, 250.0, [])
check("non multiple of 100 rejected", balance, 5000.0)
balance, message = solution.withdraw(5000.0, 10001.0, [])
check("large withdrawal rejected", balance, 5000.0)
balance, message = solution.withdraw(5000.0, 4500.0, [])
check("minimum balance enforced", balance, 5000.0)
balance, message = solution.withdraw(5000.0, 4000.0, [])
check("exact minimum allowed", balance, 1000.0)
check("two successful log entries", len(log), 2)

print("\n%d/%d tests passed." % (sum(checks), len(checks)))
