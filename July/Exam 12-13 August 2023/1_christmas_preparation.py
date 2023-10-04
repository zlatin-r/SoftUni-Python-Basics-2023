number_rolls_paper = int(input())
number_rolls_textiles = int(input())
litres_glue = float(input())
discount = int(input()) / 100

one_roll_paper = 5.80
one_roll_textiles = 7.20
one_litre_glue = 1.20

price_paper = number_rolls_paper * one_roll_paper
price_textiles = number_rolls_textiles * one_roll_textiles
price_glue = litres_glue * one_litre_glue

total_price = price_paper + price_textiles + price_glue
discount_price = total_price * discount

total = total_price - discount_price

print(f"{total:.3f}")