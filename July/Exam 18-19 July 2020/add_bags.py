price_20kg_plus = float(input())
bag_weight = float(input())
days_till_travel = int(input())
number_bags = int(input())
price = 0

if bag_weight < 10:
    price += price_20kg_plus * 0.20
elif 10 <= bag_weight <= 20:
    price += price_20kg_plus * 0.50
else:
    price = price_20kg_plus

if days_till_travel > 30:
    price *= 1.10
elif 7 <= days_till_travel <= 30:
    price *= 1.15
elif 7 > days_till_travel:
    price *= 1.40

print(f"The total price of bags is: {price * number_bags:.2f} lv. ")
