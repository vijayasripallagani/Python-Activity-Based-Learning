"""
Case Study 9: Tuple-Based Course Registration Validation
Tuples, tuple unpacking, loops, strings and conditionals.
"""

MAX_COURSES = 4
PREREQUISITES = (("CS201", "CS101"), ("CS301", "CS201"))
EXCLUSIVE_PAIRS = (("PHY101", "PHY102"),)

# A record is (roll number, tuple of course codes)
REGISTRATIONS = (
    ("R01", ("CS101", "MATH101", "PHY101", "ENG101")),
    ("R02", ("CS101", "CS201", "CS101", "MATH101")),
    ("R03", ("CS201", "MATH101")),
    ("R04", ("PHY101", "PHY102", "CS101", "ENG101", "MATH101")),
    ("R05", ("CS101", "CS201", "CS301", "MATH101")),
    ("R06", ("CS301", "MATH101")),
)


def validate(record):
    roll, courses = record
    problems = []
    if len(courses) > MAX_COURSES:
        problems.append("more than 4 courses")
    for i in range(len(courses)):
        for j in range(i + 1, len(courses)):
            if courses[i] == courses[j]:
                problems.append("duplicate " + courses[i])
    for course, needed in PREREQUISITES:
        if course in courses and needed not in courses:
            problems.append("missing " + needed + " for " + course)
    for first, second in EXCLUSIVE_PAIRS:
        if first in courses and second in courses:
            problems.append(first + " and " + second + " cannot be together")
    return problems


def main():
    valid_count = 0
    print("=" * 72)
    print("COURSE REGISTRATION VALIDATION")
    print("=" * 72)
    for record in REGISTRATIONS:
        roll, courses = record
        problems = validate(record)
        if len(problems) == 0:
            valid_count = valid_count + 1
            print(roll + " : VALID")
        else:
            detail = ""
            for problem in problems:
                if detail != "":
                    detail = detail + ", "
                detail = detail + problem
            print(roll + " : INVALID - " + detail)
    print("\nValid: %d, Invalid: %d, Total: %d" %
          (valid_count, len(REGISTRATIONS) - valid_count, len(REGISTRATIONS)))


if __name__ == "__main__":
    main()
