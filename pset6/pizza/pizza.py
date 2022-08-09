import sys
import csv
from os.path import exists
from tabulate import tabulate


def check_arguments():
    if len(sys.argv) < 2:
        sys.exit("Too few commandline arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many commandline arguments")
    else:
        fp = sys.argv[1]
        if fp[-4:] != ".csv":
            sys.exit("Not a csv file")
        else:
            if not exists(fp):
                sys.exit("File does not exist")
            return fp


def main():
    fp = check_arguments()

    table = []
    with open(fp, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            table.append(row)

    print(tabulate(table, headers="keys", tablefmt="grid"))


if __name__ == "__main__":
    main()
