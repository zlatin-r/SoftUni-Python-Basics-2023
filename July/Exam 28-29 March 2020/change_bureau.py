bitcoins = int(input())
yuan = float(input())
commission = float(input()) / 100

lev = bitcoins * 1168
yuan_to_dollar = yuan * 0.15
dollar_to_lev = yuan_to_dollar * 1.76

total_euro = (lev + dollar_to_lev) / 1.95
plus_commission = total_euro * commission
total = total_euro - plus_commission


print(f"{total:.2f}")
