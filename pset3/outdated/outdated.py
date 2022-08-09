def slash_date(d):
    pieces = d.split("/")
    try:
        mm = int(pieces[0])
        dd = int(pieces[1])
        yyyy = int(pieces[2])

        if dd > 31:
            raise

        if mm > 12:
            raise

        return [yyyy, mm, dd]
    except:
        return False


def wordy_date(d):
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    ]
    pieces = d.split(" ")
    try:
        if not "," in pieces[1]:
            raise

        mm = pieces[0]
        dd = int(pieces[1].replace(",", ""))
        yyyy = int(pieces[2])

        if not mm in months:
            raise

        if dd > 31:
            raise

        return [yyyy, months.index(mm) + 1, dd]
    except:
        return False


def print_list_as_iso8601(l):
    print(str(l[0]) + "-" + f"{l[1]:02}" + "-" + f"{l[2]:02}")
    exit(0)


while True:
    d = input("Date: ")

    pieces = slash_date(d)
    if pieces == False:
        pieces = wordy_date(d)
        if pieces == False:
            continue
        else:
            print_list_as_iso8601(pieces)
    else:
        print_list_as_iso8601(pieces)
