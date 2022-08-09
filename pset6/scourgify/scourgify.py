import sys
import csv
from os.path import exists


def check_amount_of_arguments():
    if len(sys.argv) < 3:
        sys.exit("Too few commandline arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many commandline arguments")


def check_argument_fp(i, new=False):
    fp = sys.argv[i]
    if fp[-4:] != ".csv":
        sys.exit("Not a csv file")
    else:
        if not exists(fp) and not new:
            sys.exit("File does not exist")
        return fp


def main():
    check_amount_of_arguments()
    fp_old = check_argument_fp(1, new=False)
    fp_new = check_argument_fp(2, new=True)

    with open(fp_old, "r") as file:
        with open(fp_new, "w") as file_out:
            reader = csv.DictReader(file)
            writer = csv.DictWriter(file_out, fieldnames=["first", "last", "house"])
            writer.writeheader()

            for row in reader:
                start = 1
                end = row["name"].find('"', 1, len(row))

                # full_name = row[start:end]
                full_name = row["name"]
                name_parts = full_name.split(",")
                first_name = name_parts[1].strip()
                last_name = name_parts[0].strip()

                # house = row[(end + 2) : len(row)]
                house = row["house"]

                writer.writerow(
                    {"first": first_name, "last": last_name, "house": house}
                )


if __name__ == "__main__":
    main()
