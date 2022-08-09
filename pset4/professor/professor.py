import random


def main():
    score = 0
    level = get_level()
    for i in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        correct_answer = x + y
        user_answer = -1
        tries = 0
        while user_answer != correct_answer:
            if tries > 0:
                print("EEE")

            if tries == 3:
                print(str(x) + " + " + str(y) + " = " + str(correct_answer))
                break

            try:
                tries += 1
                user_answer = int(input(str(x) + " + " + str(y) + " = "))
            except:
                continue

        if user_answer == correct_answer:
            score += 1

    print("Score: " + str(score))


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1, 2, 3]:
                break
        except:
            pass
    return level


def generate_integer(level):
    if not level in [1, 2, 3]:
        raise ValueError

    if level == 1:
        start = 0
        stop = 10
    else:
        start = 10 ** (level - 1)
        stop = 10**level - 1

    rint = random.randint(start, stop)
    return rint


if __name__ == "__main__":
    main()
