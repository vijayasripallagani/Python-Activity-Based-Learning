"""Test cases for Case Study 6."""
import solution

checks = []


def check(label, actual, expected):
    ok = actual == expected
    checks.append(ok)
    print(("PASS: " if ok else "FAIL: ") + label)


check("three runs encoded", solution.encode("aaabbbccc"), "a3b3c3")
check("single letters get count 1", solution.encode("python"), "p1y1t1h1o1n1")
check("20 repeats give two digits", solution.encode("a" * 20), "a20")
check("empty string", solution.encode(""), "")
check("alternating letters", solution.encode("ababab"), "a1b1a1b1a1b1")
check("20 a chars shrink", len(solution.encode("a" * 20)) < 20, True)
check("python grows", len(solution.encode("python")) > len("python"), True)
check("aabb has equal length", len(solution.encode("aabb")), len("aabb"))
check("mississippi encoded", solution.encode("mississippi"), "m1i1s2i1s2i1p2i1")
round_trip = True
for text in solution.SAMPLES:
    if solution.decode(solution.encode(text)) != text:
        round_trip = False
check("round trip for all samples", round_trip, True)

print("\n%d/%d tests passed." % (sum(checks), len(checks)))
