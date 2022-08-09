import random

# random.seed(123)


def is_positive_integer(s):
    if s.isdigit():
        if int(s) > 0:
            return True
    return False


def main():
    while True:
        level = input("Level: ")
        if is_positive_integer(level):
            break

    level = int(level)
    choice = random.randint(a=1, b=level)

    while True:
        guess = input("Guess: ")

        if not is_positive_integer(guess):
            continue

        guess = int(guess)

        if guess > level:
            print("Too large!")
        elif guess < level:
            print("Too small!")
        else:
            print("Just right!")
            exit(0)


if __name__ == "__main__":
    main()
