amount = float(input()) * 100
amount = int(amount)
count = 0

while amount > 0:
    if amount >= 200:
        count += amount // 200
        amount = amount % 200

    if amount >= 100:
        count += amount // 100
        amount = amount % 100

    if amount >= 50:
        count += amount // 50
        amount = amount % 50

    if amount >= 20:
        count += amount // 20
        amount = amount % 20

    if amount >= 10:
        count += amount // 10
        amount = amount % 10

    if amount >= 5:
        count += amount // 5
        amount = amount % 5

    if amount >= 2:
        count += amount // 2
        amount = amount % 2

    if amount >= 1:
        count += amount // 1
        amount = amount % 1

print(count)
