"""
Case Study 4: Advanced Numeric Pattern Generator
Nested loops, strings and validation of dimensions.
"""


def valid_size(pattern, size):
    if pattern == "diamond":
        return size >= 3 and size <= 9 and size % 2 == 1
    if pattern == "pyramid":
        return size >= 1 and size <= 9
    return False


def diamond_lines(size):
    lines = []
    widths = []
    for k in range(1, size + 1):
        widths.append(k)
    for k in range(size - 1, 0, -1):
        widths.append(k)
    for width in widths:
        parts = []
        for j in range(1, width + 1):
            if j == 1 or j == width or width == size:
                parts.append(str(j))
            else:
                parts.append(" ")
        lines.append(" " * (size - width) + " ".join(parts))
    return lines


def pyramid_lines(size):
    lines = []
    for level in range(1, size + 1):
        numbers = ""
        for j in range(1, level + 1):
            numbers = numbers + str(j)
        for j in range(level - 1, 0, -1):
            numbers = numbers + str(j)
        lines.append(" " * (size - level) + numbers)
    return lines


def main():
    samples = [("diamond", 5), ("pyramid", 4), ("diamond", 6), ("pyramid", 0)]
    for pattern, size in samples:
        print("=" * 45)
        print("%s, size %d" % (pattern, size))
        if not valid_size(pattern, size):
            print("Invalid size. Diamond needs odd 3-9; pyramid needs 1-9.")
        else:
            if pattern == "diamond":
                lines = diamond_lines(size)
            else:
                lines = pyramid_lines(size)
            for line in lines:
                print(line)


if __name__ == "__main__":
    main()
