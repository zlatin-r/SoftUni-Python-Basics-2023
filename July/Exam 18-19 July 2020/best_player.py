player_name = ""
max_goals = -999999
best_player = ""
hat_trick = False

while True:
    player_name = input()

    if player_name == "END":
        break

    goals = int(input())

    if goals > max_goals:
        max_goals = goals
        best_player = player_name

        if goals >= 3:
            hat_trick = True

    if goals >= 10:
        hat_trick = True
        break

    goals = 0

print(f"{best_player} is the best player!")

if hat_trick:
    print(f"He has scored {max_goals} goals and made a hat-trick !!!")
else:
    print(f"He has scored {max_goals} goals.")
