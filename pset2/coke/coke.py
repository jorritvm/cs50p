due = 50

while due > 0:
    print("Amount Due: ", str(due))

    coin = int(input("Insert Coin: "))
    if coin in [5, 10, 25]:
        due = due - coin

change = abs(due)
print("Change owed: " + str(change))
