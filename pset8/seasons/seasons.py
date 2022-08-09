from datetime import date, datetime
import inflect


def main():
    date_birth_str = input("Date of Birth: ")
    minutes_in_words = convert(date_birth_str)

    if minutes_in_words == False:
        print("Invalid date")
        exit(1)
    else:
        print(minutes_in_words)


def convert(date_birth_str):
    try:
        date_birth = datetime.fromisoformat(date_birth_str).date()
    except:
        return False

    minutes_passed = int((date.today() - date_birth).total_seconds() / 60)
    minutes_string = inflect.engine().number_to_words(minutes_passed, andword="")
    minutes_string = minutes_string.capitalize() + " minutes"
    return minutes_string


if __name__ == "__main__":
    main()
