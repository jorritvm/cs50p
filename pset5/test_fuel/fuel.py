def main():
    finished = False
    while not finished:
        fraction = input("Fraction: ")

        percentage = convert(fraction)
        gauge_reading = gauge(percentage)

        print(gauge_reading)


def convert(fraction):
    x, y = fraction.split("/")

    x = int(x)
    y = int(y)

    if x > y:
        raise ValueError

    if y == 0:
        raise ZeroDivisionError

    result = int(round(x / y * 100))

    return result


def gauge(percentage):
    if percentage <= 1:
        result = "E"
    elif percentage >= 99:
        result = "F"
    else:
        result = str(percentage) + "%"

    return result


if __name__ == "__main__":
    main()
