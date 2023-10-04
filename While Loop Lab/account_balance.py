installment = input()
Total = 0

while installment != "NoMoreMoney":
    current_sum = float(installment)

    if current_sum <= 0:
        print("Invalid operation!")
        break

    print(f"Increase: {current_sum:.2f}")
    Total += current_sum
    installment = input()

print(f"Total: {Total:.2f}")
