import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    expr = r"(\d{1,2}):?([0-5]\d)? (AM|PM) to (\d{1,2}):?([0-5]\d)? (AM|PM)"
    matches = re.search(expr, s)

    if matches == None:
        raise ValueError

    h1 = fix_hours(matches.group(1), matches.group(3))
    m1 = fix_minutes(matches.group(2))
    h2 = fix_hours(matches.group(4), matches.group(6))
    m2 = fix_minutes(matches.group(5))

    return h1 + ":" + m1 + " to " + h2 + ":" + m2


def fix_hours(ss, ampm):
    i = int(ss)
    i = i % 12
    if ampm.lower() == "pm":
        i = i + 12
    return f"{i:02d}"


def fix_minutes(ss):
    if ss is None:
        return "00"
    else:
        return ss


if __name__ == "__main__":
    main()
