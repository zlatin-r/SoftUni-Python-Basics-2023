budget = float(input())
sex = input()
age = int(input())
sport = input()
price = 0

if sex == "m":
    if sport == "Gym":
        price = 42
    elif sport == "Boxing":
        price = 41
    elif sport == "Yoga":
        price = 45
    elif sport == "Zumba":
        price = 34
    elif sport == "Dances":
        price = 51
    elif sport == "Pilates":
        price = 39
elif sex == "f":
    if sport == "Gym":
        price = 35
    elif sport == "Boxing":
        price = 37
    elif sport == "Yoga":
        price = 42
    elif sport == "Zumba":
        price = 31
    elif sport == "Dances":
        price = 53
    elif sport == "Pilates":
        price = 37

if age <= 19:
    discount = price * 0.20
    price -= discount

if price <= budget:
    print(f"You purchased a 1 month pass for {sport}.")
else:
    print(f"You don't have enough money! You need ${abs(price-budget):.2f} more.")
