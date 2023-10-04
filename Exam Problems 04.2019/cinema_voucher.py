voucher = int(input())
price = 0
ticket = 0
items = 0
total_tickets = 0
total_items = 0

while True:
    purchase = input()

    if purchase == "End":
        break
    elif len(purchase) > 8:
        price = ord(purchase[0]) + ord(purchase[1])
    elif len(purchase) <= 8:
        price = ord(purchase[0])

    if voucher - price >= 0:
        voucher -= price
        if len(purchase) > 8:
            ticket += 1
        elif len(purchase) <= 8:
            items += 1
    else:
        break

total_tickets += ticket
total_items += items
print(f"{total_tickets}")
print(f"{items}")
