flour_price = float(input())
flour_kilos = float(input())
sugar_kilos = float(input())
eggshells = int(input())
yeast_packages = int(input())

price_kilo_sugar = flour_price - (flour_price * 0.25)
price_eggshell = flour_price * 1.10
price_yeast = price_kilo_sugar - (price_kilo_sugar * 0.80)

total_price = ((flour_price * flour_kilos) + (price_kilo_sugar * sugar_kilos) + (price_eggshell * eggshells) +
               (price_yeast * yeast_packages))

print(f"{total_price:.2f}")

