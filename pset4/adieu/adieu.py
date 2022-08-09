def get_names():

    names = list()
    while True:
        try:
            name = input("Name: ")
            names.append(name)

        except EOFError:
            print_names(names)
            exit(0)


def print_names(names):
    if len(names) == 1:
        suffix = names[0]
    elif len(names) == 2:
        suffix = names[0] + " and " + names[1]
    else:
        suffix = ", ".join(names[0:-1]) + ", and " + names[-1]

    print("\nAdieu, adieu, to " + suffix)


get_names()
