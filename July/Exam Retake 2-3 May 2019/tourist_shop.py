budget = float(input())
product_name = input()
product_price = float(input())
counter = 1
count_products = 0
total = 0

while True:
    count_products += 1

    if counter == 3:
        product_price /= 2
        counter = 0

    total += product_price

    if product_price > budget:
        print("You don't have enough money!")
        print(f"You need {product_price - budget:.2f} leva!")
        break

    budget -= product_price
    counter += 1
    product_name = input()

    if product_name == "Stop":
        print(f"You bought {count_products} products for {total:.2f} leva.")
        break

    product_price = float(input())
