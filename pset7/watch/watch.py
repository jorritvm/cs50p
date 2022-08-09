import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    expr = r"<iframe.*src=\".*?youtube.*?/embed/(.*?)\".*</iframe>"
    id = re.search(expr, s, re.IGNORECASE)

    if id is None:
        return id
    else:
        id = id.group(1)
        new_url = f"https://youtu.be/{id}"
        return new_url


if __name__ == "__main__":
    main()
