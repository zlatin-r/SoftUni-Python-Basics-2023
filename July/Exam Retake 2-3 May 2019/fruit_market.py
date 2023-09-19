strawberries_price = float(input())
amount_bananas = float(input())
amount_oranges = float(input())
amount_raspberries = float(input())
amount_strawberries = float(input())

strawberries = strawberries_price * amount_strawberries

raspberries_price = strawberries_price / 2
raspberries = raspberries_price * amount_raspberries

oranges_price = raspberries_price * 0.60
oranges = oranges_price * amount_oranges

bananas_price = raspberries_price * 0.20
bananas = bananas_price * amount_bananas

total = strawberries + raspberries + oranges + bananas
print(f"{total:.2f}")