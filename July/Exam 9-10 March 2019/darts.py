player_name = input()
player_points = 301
command = input()
unsuccessful = 0
successful = 0

while command != "Retire":
    points = int(input())

    if command == "Single":
        if player_points - points < 0:
            unsuccessful += 1
            pass
        else:
            player_points -= points
            successful += 1

    elif command == "Double":
        if player_points - points * 2 < 0:
            unsuccessful += 1
            pass
        else:
            player_points -= points * 2
            successful += 1

    elif command == "Triple":
        if player_points - points * 3 < 0:
            unsuccessful += 1
            pass
        else:
            player_points -= points * 3
            successful += 1

    if player_points == 0:
        break
    else:
        command = input()

if player_points == 0:
    print(f"{player_name} won the leg with {successful} shots.")
else:
    print(f"{player_name} retired after {unsuccessful} unsuccessful shots.")
