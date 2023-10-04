stadium_capacity = int(input())
total_fans = int(input())

sec_A = 0
sec_B = 0
sec_V = 0
sec_G = 0

for i in range(total_fans):
    sector = input()

    if sector == "A":
        sec_A += 1
    elif sector == "B":
        sec_B += 1
    elif sector == "V":
        sec_V += 1
    elif sector == "G":
        sec_G += 1

print(f"{(sec_A / total_fans) * 100:.2f}%")
print(f"{(sec_B / total_fans) * 100:.2f}%")
print(f"{(sec_V / total_fans) * 100:.2f}%")
print(f"{(sec_G / total_fans) * 100:.2f}%")
print(f"{(total_fans / stadium_capacity) * 100:.2f}%")
