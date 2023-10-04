trip_price = float(input())

count_puzzle = int(input())
count_dolls = int(input())
count_teddy_bear = int(input())
count_minions = int(input())
count_trucks = int(input())

count_all = count_puzzle + count_dolls + count_teddy_bear + count_minions + count_trucks
price_all = (count_puzzle * 2.60) + (count_dolls * 3) + (count_teddy_bear * 4.10) + (count_minions * 8.20) + (
        count_trucks * 2)

if count_all >= 50:
    price_all -= price_all * 0.25
price_all -= price_all * 0.10
if price_all >= trip_price:
    print(f'Yes! {abs(price_all-trip_price):.2f} lv left.')
elif price_all<trip_price:
    print(f"Not enough money! {abs(price_all-trip_price):.2f} lv needed.")