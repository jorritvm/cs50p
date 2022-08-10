import random


def main():
    while True:
        try:
            level = int(input("Level: "))
        except ValueError:
            continue
        if level > 0:
            break
    choice = random.randint(1, level)

    while True:
        try:
            guess = int(input("Guess: "))
        except ValueError:
            continue
        else:
            if guess > choice:
                print("Too large!", end="")
                continue
            elif guess < choice:
                print("Too small!", end="")
                continue
            else:
                print("Just right!", end="")
                break


if __name__ == "__main__":
    main()
