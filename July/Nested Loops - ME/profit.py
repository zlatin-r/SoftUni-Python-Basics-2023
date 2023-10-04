coins_1 = int(input())
coins_2 = int(input())
banknote_5 = int(input())
bill = int(input())

for i in range(coins_1 + 1):
    for j in range(coins_2 + 1):
        for k in range(banknote_5 + 1):

            if (i * 1) + (j * 2) + (k * 5) == bill:
                print(f"{i} * 1 lv. + {j} * 2 lv. + {k} * 5 lv. = {bill} lv.")
