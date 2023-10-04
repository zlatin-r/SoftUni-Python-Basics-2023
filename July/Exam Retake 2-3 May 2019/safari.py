budget = float(input())
fuel_needed = float(input())
day = input()

price_fuel = fuel_needed * 2.10
price_tour_guide = 100
total_price = price_fuel + price_tour_guide

if day == "Saturday":
    total_price *= 0.90
elif day == "Sunday":
    total_price *= 0.80

if total_price <= budget:
    print(f"Safari time! Money left: {budget - total_price:.2f} lv. ")
else:
    print(f"Not enough money! Money needed: {total_price - budget:.2f} lv.")