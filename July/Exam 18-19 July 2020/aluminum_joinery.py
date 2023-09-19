number_windows = int(input())
price = 0

type_windows = input()
if type_windows == "90X130":
    price = 110 * number_windows

    if number_windows > 60:
        price -= price * 0.08
    elif number_windows > 30:
        price -= (price * 0.05)

elif type_windows == "100X150":
    price = 140 * number_windows

    if number_windows > 80:
        price -= price * 0.10
    elif number_windows > 40:
        price -= (price * 0.06)

elif type_windows == "130X180":
    price = 190 * number_windows

    if number_windows > 50:
        price -= price * 0.12
    elif number_windows > 20:
        price -= (price * 0.07)

elif type_windows == "200X300":
    price = 250 * number_windows

    if number_windows > 50:
        price -= price * 0.14
    elif number_windows > 25:
        price -= (price * 0.09)

delivery = input()
if delivery == "With delivery":
    price += 60
elif delivery == "Without delivery":
    pass

if number_windows < 10:
    print("Invalid order")
elif number_windows > 99:
    price -= price * 0.04
    print(f"{price:.2f} BGN")
else:
    print(f"{price:.2f} BGN")
