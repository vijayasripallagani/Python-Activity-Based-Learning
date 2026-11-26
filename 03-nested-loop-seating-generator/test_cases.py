"""Test cases for Case Study 3."""
import solution

checks = []


def check(label, actual, expected):
    ok = actual == expected
    checks.append(ok)
    print(("PASS: " if ok else "FAIL: ") + label)


grid = solution.build_seating(solution.ROWS, solution.COLS, solution.RESERVED)
check("6 rows in the grid", len(grid), 6)
check("8 columns in every row", len(grid[0]), 8)
check("(2,3) is reserved", grid[1][2], "R")
check("(4,5) is reserved", grid[3][4], "R")
check("(2,1) blocked by alternate rule", grid[1][0], "X")
check("(2,2) is a student seat", grid[1][1], "S")
check("(4,5) reserved although odd column", grid[3][4], "R")
check("free seat accepted", solution.is_seat_free(grid, 3, 4), True)
check("reserved seat rejected", solution.is_seat_free(grid, 2, 3), False)
check("out of range seat rejected", solution.is_seat_free(grid, 9, 2), False)
check("student seats counted", solution.count_seats(grid, "S"), 36)
check("all seats accounted for",
      solution.count_seats(grid, "S") + solution.count_seats(grid, "R")
      + solution.count_seats(grid, "X"), 48)

print("\n%d/%d tests passed." % (sum(checks), len(checks)))
