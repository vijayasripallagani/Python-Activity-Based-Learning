"""
Case Study 5: Password Policy Validation Engine
String scanning, loops and conditional checks.
"""

SPECIALS = "!@#$%"
MIN_LENGTH = 8
BAD_WORDS = ["password", "admin"]


def validate(password):
    failures = []
    upper = False
    lower = False
    digit = False
    special = False

    for ch in password:
        if "A" <= ch <= "Z":
            upper = True
        elif "a" <= ch <= "z":
            lower = True
        elif "0" <= ch <= "9":
            digit = True
        elif ch in SPECIALS:
            special = True

    if len(password) < MIN_LENGTH:
        failures.append("length below 8")
    if not upper:
        failures.append("missing uppercase")
    if not lower:
        failures.append("missing lowercase")
    if not digit:
        failures.append("missing digit")
    if not special:
        failures.append("missing special character")

    for i in range(len(password) - 2):
        if password[i] == password[i + 1] and password[i] == password[i + 2]:
            failures.append("three identical characters in a row")
            break

    small = password.lower()
    for word in BAD_WORDS:
        if word in small:
            failures.append("prohibited word: " + word)
    return failures


def main():
    samples = ["MyCampus#2026", "short", "lowercase1!", "UPPER123!",
               "Campus2026", "Admin#123", "Camp#aaa2026"]
    print("=" * 66)
    print("PASSWORD POLICY CHECK")
    print("=" * 66)
    accepted = 0
    for password in samples:
        failures = validate(password)
        if len(failures) == 0:
            accepted = accepted + 1
            print("%-16s PASS" % password)
        else:
            detail = ""
            for failure in failures:
                if detail != "":
                    detail = detail + ", "
                detail = detail + failure
            print("%-16s FAIL: %s" % (password, detail))
    print("Accepted %d of %d sample passwords." % (accepted, len(samples)))


if __name__ == "__main__":
    main()
