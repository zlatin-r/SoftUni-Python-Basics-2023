eggs = int(input())
red = 0
orange = 0
blue = 0
green = 0
max_eggs = -9999
max_col = ""

for i in range(eggs):
    color = input()

    if color == "red":
        red += 1
    elif color == "orange":
        orange += 1
    elif color == "blue":
        blue += 1
    elif color == "green":
        green += 1

    if red > max_eggs:
        max_eggs = red
        max_col = "red"
    if orange > max_eggs:
        max_eggs = orange
        max_col = "orange"
    if blue > max_eggs:
        max_eggs = blue
        max_col = "blue"
    if green > max_eggs:
        max_eggs = green
        max_col = "green"

print(f"Red eggs: {red}")
print(f"Orange eggs: {orange}")
print(f"Blue eggs: {blue}")
print(f"Green eggs: {green}")
print(f"Max eggs: {max_eggs} -> {max_col}")

