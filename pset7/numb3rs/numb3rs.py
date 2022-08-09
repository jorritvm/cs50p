import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    elements = ip.split(".")

    if len(elements) != 4:
        return False

    for element in elements:
        try:
            i = int(element)
            if i < 0 or i > 255:
                return False
        except:
            return False

    return True


if __name__ == "__main__":
    main()
