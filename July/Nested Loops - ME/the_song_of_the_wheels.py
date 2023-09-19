control_value = int(input())
count = 0
password = 0

for a in range(1, 10):
    for b in range(1, 10):
        for c in range(1, 10):
            for d in range(1, 10):
                if a * b + c * d == control_value and a < b and c > d:
                    count += 1
                    print(f"{a}{b}{c}{d}", end=" ")
                    if count == 4:
                        password = f"{a}{b}{c}{d}"
print()
if count >= 4:
    print(f"Password: {password}")
else:
    print("No!")
