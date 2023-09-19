budget = float(input())
count_statists = float(input())
price_clothing_for_one_statitst = float(input())
decor_price = budget * 0.10
clothing_price = count_statists * price_clothing_for_one_statitst

if count_statists > 150:
    clothing_price = clothing_price - (clothing_price * 0.10)

money_needed = abs(budget-(decor_price+clothing_price))
money_rest = budget-(decor_price+clothing_price)

if decor_price + clothing_price > budget:
    print('Not enough money!')
    print(f'Wingard needs {money_needed:.2f} leva more.')

else:
    print('Action!')
    print(f'Wingard starts filming with {money_rest:.2f} leva left.')