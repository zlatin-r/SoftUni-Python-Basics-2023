budget = float(input())

count_v_cards = int(input())
count_processors = int(input())
count_ram = int(input())

price_v_cards = count_v_cards * 250
price_processor = (price_v_cards * 0.35) * count_processors
price_ram = (price_v_cards * 0.10) * count_ram

price_all = (price_v_cards + price_ram + price_processor)
if count_v_cards > count_processors:
    price_all -= price_all * 0.15
if price_all <= budget:
    print(f"You have {(budget - price_all):.2f} leva left!")
else:
    print(f"Not enough money! You need {abs(budget - price_all):.2f} leva more!")
