def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    return (
        start_with_two_letters(s)
        and allowed_char_count(s)
        and numbers_at_end(s)
        and no_illegal_signs(s)
        and first_num_not_zero(s)
    )


def start_with_two_letters(s):
    valid = False
    if s[0].isalpha():
        if len(s) > 1:
            if s[1].isalpha():
                valid = True
    return valid


def allowed_char_count(s):
    return len(s) >= 2 and len(s) <= 6


def numbers_at_end(s):
    valid = True
    has_num = False
    for subs in s:
        if subs.isdigit():
            has_num = True
        if subs.isalpha() and has_num == True:
            valid = False
    return valid


def no_illegal_signs(s):
    valid = True
    for subs in s:
        if not subs.isalpha() and not subs.isdigit():
            valid = False
    return valid


def first_num_not_zero(s):
    valid = True
    for subs in s:
        if subs.isdigit():
            if subs == "0":
                valid = False
            break
    return valid


if __name__ == "__main__":
    main()
