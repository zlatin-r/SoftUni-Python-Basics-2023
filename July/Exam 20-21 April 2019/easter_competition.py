kozunaks = int(input())
kozunaks_points = 0
best_backer = ""
points = 0
max_points = -99999

for i in range(kozunaks):
    backer_name = input()

    while points != "Stop":
        kozunaks_points += int(points)
        points = input()

    print(f"{backer_name} has {kozunaks_points} points.")

    if kozunaks_points > max_points:
        max_points = kozunaks_points
        best_backer = backer_name
        print(f"{backer_name} is the new number 1!")

    points = 0
    kozunaks_points = 0

print(f"{best_backer} won competition with {max_points} points!")
