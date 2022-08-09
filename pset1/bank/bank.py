greeting = input("Greeting: ")

greeting = greeting.lower().strip()

if greeting[0:5] == "hello":
    out = "$0"
elif greeting[0] == "h":
    out = "$20"
else:
    out = "$100"

print(out)
