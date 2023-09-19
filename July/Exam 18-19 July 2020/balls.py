from math import floor

number_balls = int(input())
points = 0
red_b, orange_b, yellow_b, white_b, black_b = 0, 0, 0, 0, 0
other_colors = 0


for i in range(number_balls):
    color = input()

    if color == "red":
        points += 5
        red_b += 1
    elif color == "orange":
        points += 10
        orange_b += 1
    elif color == "yellow":
        points += 15
        yellow_b += 1
    elif color == "white":
        points += 20
        white_b += 1
    elif color == "black":
        points /= 2
        floor(points)
        black_b += 1
    else:
        other_colors += 1
        continue

print(f"Total points: {floor(points)}")
print(f"Red balls: {red_b}")
print(f"Orange balls: {orange_b}")
print(f"Yellow balls: {yellow_b}")
print(f"White balls: {white_b}")
print(f"Other colors picked: {other_colors}")
print(f"Divides from black balls: {black_b}")

