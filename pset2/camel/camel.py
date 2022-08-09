txt = input("Enter something in camelCase: ")

output = list()
for i in range(len(txt)):
    letter = txt[i]
    if letter.isupper():
        output.append("_")
    output.append(letter.lower())
print("".join(output))
