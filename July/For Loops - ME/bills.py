months = int(input())
electricity = 0
other = 0
total_electricity = 0
total_water = 0
total_internet = 0
total_other = 0
total = 0

for i in range(months):
    electricity = float(input())
    water = 20
    internet = 15

    ewi = electricity + water + internet
    other = ewi * 1.20

    total_electricity += electricity
    total_water += water
    total_internet += internet
    total_other += other

total += total_electricity + total_water + total_internet + total_other

print(f"Electricity: {total_electricity:.2f} lv")
print(f"Water: {total_water:.2f} lv")
print(f"Internet: {total_internet:.2f} lv")
print(f"Other: {total_other:.2f} lv")
print(f"Average: {total / months:.2f} lv")
