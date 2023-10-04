sum_money = int(input())
counter = 0
count_cash = 0
sum_cash = 0
count_check = 0
sum_check = 0
sold = True

while sum_money > 0:
    counter += 1
    product_price = input()

    if counter % 2 == 0:
        cash = False
        count_check += 1
    else:
        cash = True
        count_cash += 1

    if product_price == "End":
        sold = False
        break
    else:
        if cash and int(product_price) > 100:
            count_cash -= 1
            print("Error in transaction!")
        elif not cash and int(product_price) < 10:
            count_check -= 1
            print("Error in transaction!")
        else:
            if cash:
                sum_cash += int(product_price)
            else:
                sum_check += int(product_price)
            print("Product sold!")
            sum_money -= int(product_price)

if sold:
    print(f"Average CS: {(sum_cash / count_cash):.2f}")
    print(f"Average CC: {(sum_check / count_check):.2f}")
else:
    print("Failed to collect required money for charity.")

