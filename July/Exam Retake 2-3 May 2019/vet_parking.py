days = int(input())
hours = int(input())
price = 0
total = 0

for i in range(1, days + 1):
    if i % 2 == 0:
        for j in range(1, hours + 1):
            if j % 2 == 1:
                price += 2.50
            else:
                price += 1
    else:
        for j in range(1, hours + 1):
            if j % 2 == 0:
                price += 1.25
            else:
                price += 1
    total += price
    print(f"Day: {i} - {price:.2f} leva")
    price = 0
print(f"Total: {total:.2f} leva")
