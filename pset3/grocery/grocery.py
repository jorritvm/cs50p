def get_shopping_list():

    shopping_list = dict()
    while True:
        try:
            item = input().upper()
            if item in shopping_list:
                shopping_list[item] += 1
            else:
                shopping_list[item] = 1

        except EOFError:
            for item in sorted(shopping_list.keys()):
                print(str(shopping_list[item]) + " " + item)
            exit(0)


get_shopping_list()
