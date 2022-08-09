def get_user_choice_cost():
    menu = {
        "Baja Taco": 4.00,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00,
    }
    while True:
        try:
            return float(menu[input("Order: ").title()])
        except KeyError:
            pass


def get_order():

    bill = 0
    while True:
        try:
            order_cost = get_user_choice_cost()

            bill += order_cost
            print("Total: $" + "{:.2f}".format(bill))

        except EOFError:
            print("\n")
            exit(0)


get_order()
