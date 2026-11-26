"""
Case Study 3: Nested Loop Examination Seating Generator
Nested lists, nested loops, tuples and conditional statements.
"""

ROWS = 6
COLS = 8
RESERVED = [(2, 3), (4, 5), (6, 7)]   # (row, column), both start at 1


def build_seating(rows, cols, reserved):
    grid = []
    for r in range(1, rows + 1):
        row_seats = []
        for c in range(1, cols + 1):
            seat = (r, c)
            if seat in reserved:
                row_seats.append("R")
            elif r % 2 == 0 and c % 2 == 1:
                row_seats.append("X")
            else:
                row_seats.append("S")
        grid.append(row_seats)
    return grid


def count_seats(grid, symbol):
    total = 0
    for row in grid:
        for seat in row:
            if seat == symbol:
                total = total + 1
    return total


def is_seat_free(grid, row, column):
    if row < 1 or row > len(grid):
        return False
    if column < 1 or column > len(grid[0]):
        return False
    return grid[row - 1][column - 1] == "S"


def print_seating(grid):
    header = "      "
    for c in range(1, len(grid[0]) + 1):
        header = header + str(c) + " "
    print(header)
    for r in range(len(grid)):
        line = "R" + str(r + 1) + "  |  "
        for seat in grid[r]:
            line = line + seat + "  "
        print(line)
    print("S = student seat, R = reserved, X = alternate rule")


def main():
    grid = build_seating(ROWS, COLS, RESERVED)
    print("=" * 50)
    print("EXAMINATION SEATING ARRANGEMENT")
    print("=" * 50)
    print_seating(grid)
    print("Students: %d, Reserved: %d, Blocked: %d" %
          (count_seats(grid, "S"), count_seats(grid, "R"), count_seats(grid, "X")))
    for row, column in [(2, 2), (3, 4), (2, 3), (9, 2)]:
        print("Seat (%d,%d) available: %s" % (row, column, is_seat_free(grid, row, column)))


if __name__ == "__main__":
    main()
