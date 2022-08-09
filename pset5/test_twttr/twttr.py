def main():
    txt = input("Input: ")
    print(shorten(txt))


def shorten(word):
    output = list()
    for i in range(len(word)):
        letter = word[i]
        if not letter in ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]:
            output.append(letter)
    return "".join(output)


if __name__ == "__main__":
    main()
