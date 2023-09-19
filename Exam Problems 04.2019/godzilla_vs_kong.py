budget = float(input())
statists = int(input())
clothing = float(input())
decor = budget - (budget * 0.90)

if statists > 150:
    discount = clothing - (clothing * 0.90)
    statists_clothing = statists *(clothing - discount)
else:
    statists_clothing = statists * clothing

total = statists_clothing + decor

if budget - total < 0:
    print("Not enough money!")
    print(f"Wingard needs {abs(budget - total):.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {abs(budget - total):.2f} leva left.")


