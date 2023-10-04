party_budget = float(input())
number_love_letters = int(input())
number_wax_roses = int(input())
number_key_holders = int(input())
number_cartoons = int(input())
number_surprises = int(input())

price_love_letters = 0.60
price_wax_roses = 7.20
price_key_holders = 3.60
price_cartoons = 18.20
price_surprises = 22
discount = 0

count = number_love_letters + number_wax_roses + number_key_holders + number_surprises + number_cartoons

sum_love_letters = number_love_letters * price_love_letters
sum_wax_roses = number_wax_roses * price_wax_roses
sum_key_holders = number_key_holders * price_key_holders
sum_cartoons = number_cartoons * price_cartoons
sum_surprises = number_surprises * price_surprises

total_sum = sum_love_letters + sum_wax_roses + sum_key_holders + sum_cartoons + sum_surprises

if count >= 25:
    discount = total_sum * 0.35
    total_sum -= discount

maiden_party_cost = total_sum * 0.10
total_sum -= maiden_party_cost

if total_sum >= party_budget:
    print(f"Yes! {total_sum - party_budget:.2f} lv left.")
else:
    print(f"Not enough money! {abs(total_sum - party_budget):.2f} lv needed.")

