txt = input("Input: ")

output = list()
for i in range(len(txt)):
    letter = txt[i]
    if not letter in ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]:
        output.append(letter)
print("".join(output))
