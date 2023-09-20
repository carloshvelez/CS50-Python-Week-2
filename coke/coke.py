due = 50
while True:
    coin = int(input("Insert Coin: "))

    if coin != 5 and coin != 10 and coin != 25:
        print(f"Amount Due: {due}")
        continue

    due = due - coin
    if due > 0:
        print(f"Amount Due: {due}")

    else:
        print(f"Change Owed: {due * -1}")
        break

