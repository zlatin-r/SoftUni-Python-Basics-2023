clients = int(input())
items = 0
price = 0
client_spend = 0
total_spend = 0

for i in range(clients):
    decoration = input()

    while decoration != "Finish":
        if decoration == "basket":
            price = 1.50
        elif decoration == "wreath":
            price = 3.80
        elif decoration == "chocolate bunny":
            price = 7

        items += 1
        client_spend += price
        decoration = input()

    if items % 2 == 0:
        client_spend -= (client_spend * 0.20)

    print(f"You purchased {items} items for {client_spend:.2f} leva.")
    total_spend += client_spend
    items = 0
    price = 0
    client_spend = 0
print(f"Average bill per client is: {total_spend / clients:.2f} leva.")
