stage = input()
ticket = input()
number_tickets = int(input())
picture = input()
price = 0

if stage == "Quarter final":
    if ticket == "Standard":
        price = 55.50 * number_tickets
    elif ticket == "Premium":
        price = 105.20 * number_tickets
    elif ticket == "VIP":
        price = 118.90 * number_tickets

elif stage == "Semi final":
    if ticket == "Standard":
        price = 75.88 * number_tickets
    elif ticket == "Premium":
        price = 125.22 * number_tickets
    elif ticket == "VIP":
        price = 300.40 * number_tickets

elif stage == "Final":
    if ticket == "Standard":
        price = 110.10 * number_tickets
    elif ticket == "Premium":
        price = 160.66 * number_tickets
    elif ticket == "VIP":
        price = 400 * number_tickets

if price > 4000:
    price *= 0.75
    if picture == "Y":
        price -= 40 * number_tickets
elif 2500 < price:
    price *= 0.90

if picture == "Y":
    price += number_tickets * 40

print(f"{price:.2f}")
