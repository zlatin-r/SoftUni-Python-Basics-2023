year_tax = int(input())

shoes = year_tax * 0.60
clothes = shoes * 0.80
ball = clothes * 0.25
accessories = ball * 0.20

total = shoes + clothes + ball + accessories + year_tax

print(f"{total:.2f}")
