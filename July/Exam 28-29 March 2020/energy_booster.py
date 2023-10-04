flavor = input()
set_size = input()
number_of_sets = int(input())
price = 0

if set_size == "small":
    if flavor == "Watermelon":
        price = 56 * 2
    elif flavor == "Mango":
        price = 36.66 * 2
    elif flavor == "Pineapple":
        price = 42.10 * 2
    elif flavor == "Raspberry":
        price = 20 * 2

elif set_size == "big":
    if flavor == "Watermelon":
        price = 28.70 * 5
    elif flavor == "Mango":
        price = 19.60 * 5
    elif flavor == "Pineapple":
        price = 24.80 * 5
    elif flavor == "Raspberry":
        price = 15.20 * 5

total_price = number_of_sets * price

if 400 <= total_price <= 1000:
    discount = total_price * 0.15
    total_price -= discount
elif 1000 < total_price:
    discount = total_price * 0.50
    total_price -= discount

print(f"{total_price:.2f} lv.")