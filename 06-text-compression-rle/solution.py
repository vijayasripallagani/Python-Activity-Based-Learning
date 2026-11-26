"""
Case Study 6: Text Compression Using Character Runs
Strings, loops, operators and lists of records.
"""

SAMPLES = ["aaabbbccc", "python", "aaaaaaaaaaaaaaaaaaaa", "ababab", "mississippi"]


def encode(text):
    result = ""
    i = 0
    while i < len(text):
        character = text[i]
        count = 0
        while i < len(text) and text[i] == character:
            count = count + 1
            i = i + 1
        result = result + character + str(count)
    return result


def decode(text):
    result = ""
    i = 0
    while i < len(text):
        character = text[i]
        i = i + 1
        digits = ""
        while i < len(text) and "0" <= text[i] <= "9":
            digits = digits + text[i]
            i = i + 1
        for j in range(int(digits)):
            result = result + character
    return result


def main():
    print("=" * 64)
    print("RUN LENGTH ENCODING")
    print("=" * 64)
    for text in SAMPLES:
        coded = encode(text)
        change = len(coded) - len(text)
        if change < 0:
            note = "saves %d characters" % (-change)
        elif change > 0:
            note = "grows by %d characters" % change
        else:
            note = "same length"
        print("%-21s -> %-24s %d -> %d (%s)" %
              (text, coded, len(text), len(coded), note))
        if decode(coded) != text:
            print("Decoding check failed!")


if __name__ == "__main__":
    main()
