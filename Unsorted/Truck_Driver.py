seasons = input()
km_month = float(input())

paycheck = 0

if km_month <= 5000:
    if seasons == "Spring" or seasons == "Autumn":
        paycheck = km_month * 0.75
    elif seasons == "Summer":
        paycheck = km_month * 0.90
    elif seasons == "Winter":
        paycheck = km_month * 1.05

if 5000 < km_month <= 10000:
    if seasons == "Spring" or seasons == "Autumn":
        paycheck = km_month * 0.95
    elif seasons == "Summer":
        paycheck = km_month * 1.10
    elif seasons == "Winter":
        paycheck = km_month * 1.25

if 10000 < km_month <= 20000:
    paycheck = km_month * 1.45

paycheck *= 0.90
print(f"{(paycheck * 4):.2f}")
