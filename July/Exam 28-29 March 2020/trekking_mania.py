groups = int(input())
musala = 0
mont_blanc = 0
kilimanjaro = 0
K2 = 0
everest = 0
total_climbers = 0

for i in range(groups):
    climbers = int(input())
    total_climbers += climbers

    if climbers <= 5:
        musala += climbers
    elif 6 <= climbers <= 12:
        mont_blanc += climbers
    elif 13 <= climbers <= 25:
        kilimanjaro += climbers
    elif 26 <= climbers <= 40:
        K2 += climbers
    elif 41 <= climbers:
        everest += climbers

print(f"{musala / total_climbers * 100:.2f}%")
print(f"{mont_blanc / total_climbers * 100:.2f}%")
print(f"{kilimanjaro / total_climbers * 100:.2f}%")
print(f"{K2 / total_climbers * 100:.2f}%")
print(f"{everest / total_climbers * 100:.2f}%")
