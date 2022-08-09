import sys


def check_arguments():
    if len(sys.argv) < 2:
        sys.exit("Too few commandline arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many commandline arguments")
    else:
        fp = sys.argv[1]
        if fp[-3:] != ".py":
            sys.exit("Not a python file")
        else:
            return fp


def main():
    fp = check_arguments()

    with open(fp, "r") as file:
        lines = file.readlines()

    loc = 0
    for line in lines:
        if line.strip() == "":
            continue
        elif line.strip()[0] == "#":
            continue
        else:
            loc += 1

    print(loc)


if __name__ == "__main__":
    main()
