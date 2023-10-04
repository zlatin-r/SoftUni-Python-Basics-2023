days = int(input())
hours = int(input())
total = 0

for i in range(1, days + 1):
    bill = 0

    if i % 2 == 0:
        for j in range(1, hours + 1):
            if j % 2 == 1:
                bill += 2.50
            else:
                bill += 1.00
        total += bill
        print(f"Day: {i} - {bill:.2f} leva")

    else:
        for k in range(1, hours + 1):
            if k % 2 == 0:
                bill += 1.25
            else:
                bill += 1.00
        total += bill
        print(f"Day: {i} - {bill:.2f} leva")

print(f"Total: {total:.2f} leva")
