from validator_collection import validators, checkers, errors


def main():
    print(validate(input("What's your email address? ")))


def validate(s):
    try:
        email_address = validators.email(s)
        return "Valid"
    except:
        return "Invalid"


if __name__ == "__main__":
    main()
