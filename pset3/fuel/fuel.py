def ask_and_answer_user():
    try:
        user_input = input("Fraction: ")
        x, y = user_input.split("/")

        x = int(x)
        y = int(y)
        result = round(x / y * 100)

        if result <= 1:
            result = "E"
        elif result > 100:
            return False
        elif result >= 99:
            result = "F"
        else:
            result = str(result) + "%"

        print(result)
        return True

    except (ValueError, ZeroDivisionError):
        return False


finished = False
while not finished:
    finished = ask_and_answer_user()
