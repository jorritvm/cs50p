def main():
    time = input("What time is it? ")
    decimal_time = convert(time)

    if decimal_time >= 7 and decimal_time <= 8:
        print("breakfast time")
    elif decimal_time >= 12 and decimal_time <= 13:
        print("lunch time")
    elif decimal_time >= 18 and decimal_time <= 19:
        print("dinner time")


def convert(time):
    timelist = time.split(sep=":")
    hour = float(timelist[0])
    minutes_fraction = float(timelist[1]) / 60
    return hour + minutes_fraction


if __name__ == "__main__":
    main()
