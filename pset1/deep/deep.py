answer = input(
    "What is the Answer to the Great Question of Life, the Universe, and Everything? "
)

answer = answer.strip().lower()

if answer == "42":
    out = "Yes"
elif answer == "forty-two":
    out = "Yes"
elif answer == "forty two":
    out = "Yes"
else:
    out = "No"

print(out)
