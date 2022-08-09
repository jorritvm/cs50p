def convert(str_input):
    str_converted = str_input.replace(":)", "🙂")
    str_converted = str_converted.replace(":(", "🙁")
    return str_converted


def main():
    str_input = input()
    str_converted = convert(str_input)
    print(str_converted)


main()
