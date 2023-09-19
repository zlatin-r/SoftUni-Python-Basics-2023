eggs_size = input()
color = input()
amount = int(input())
total_price = 0

if eggs_size == "Large":
    if color == "Red":
        total_price = 16 * amount
    elif color == "Green":
        total_price = 12 * amount
    elif color == "Yellow":
        total_price = 9 * amount

elif eggs_size == "Medium":
    if color == "Red":
        total_price = 13 * amount
    elif color == "Green":
        total_price = 9 * amount
    elif color == "Yellow":
        total_price = 7 * amount

elif eggs_size == "Small":
    if color == "Red":
        total_price = 9 * amount
    elif color == "Green":
        total_price = 8 * amount
    elif color == "Yellow":
        total_price = 5 * amount

final_price = total_price - (total_price * 0.35)

print(f"{final_price:.2f} leva.")