chrysanthemums = int(input())
roses = int(input())
tulips = int(input())
season = input()
holiday = input()

total_price = 0
price_chrysanthemums = 0
price_roses = 0
price_tulips = 0

if season == "Summer":
    price_chrysanthemums = chrysanthemums * 2.00
    price_roses = roses * 4.10
    price_tulips = tulips * 2.50
    total_price = price_chrysanthemums + price_roses + price_tulips

if season == "Spring":
    price_chrysanthemums = chrysanthemums * 2.00
    price_roses = roses * 4.10
    price_tulips = tulips * 2.50
    total_price = price_chrysanthemums + price_roses + price_tulips
    if tulips > 7:
        total_price *= 0.95

if season == "Winter":
    price_chrysanthemums = chrysanthemums * 3.75
    price_roses = roses * 4.50
    price_tulips = tulips * 4.15
    total_price = price_chrysanthemums + price_roses + price_tulips
    if roses >= 10:
        total_price *= 0.90

if season == "Autumn":
    price_chrysanthemums = chrysanthemums * 3.75
    price_roses = roses * 4.50
    price_tulips = tulips * 4.15
    total_price = price_chrysanthemums + price_roses + price_tulips

if chrysanthemums + roses + tulips > 20:
    total_price *= 0.80

if holiday == "Y":
    total_price += total_price * 0.15

print(f"{(total_price + 2):.2f}")
