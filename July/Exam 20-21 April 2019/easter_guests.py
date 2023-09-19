from math import ceil

guests = int(input())
budget = int(input())

eggs_price = (guests * 2) * 0.45
kozunaks_price = (ceil(guests / 3)) * 4
total_price = kozunaks_price + eggs_price

if total_price > budget:
    print(f"Lyubo doesn't have enough money.")
    print(f"He needs {total_price - budget:.2f} lv. more.")
elif total_price <= budget:
    print(f"Lyubo bought {ceil(guests / 3)} Easter bread and {guests * 2} eggs.")
    print(f"He has {budget - total_price:.2f} lv. left.")
