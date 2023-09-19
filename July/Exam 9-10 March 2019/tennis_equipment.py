from math import ceil, floor

racket_price = float(input())
number_rackets = int(input())
number_sneakers = int(input())

price_sneakers = racket_price / 6

total_shoes_rackets = (racket_price * number_rackets) + (price_sneakers * number_sneakers)
accessories = total_shoes_rackets * 0.20
djokovic_price = (total_shoes_rackets + accessories) / 8
sponsors_price = (total_shoes_rackets + accessories) - djokovic_price

print(f"Price to be paid by Djokovic {floor(djokovic_price)}")
print(f"Price to be paid by sponsors {ceil(sponsors_price)}")
