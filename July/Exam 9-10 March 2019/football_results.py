game_1 = input()
game_2 = input()
game_3 = input()
won = 0
lost = 0
draw = 0

if int(game_1[0]) > int(game_1[2]):
    won += 1
elif int(game_1[0]) < int(game_1[2]):
    lost += 1
elif int(game_1[0]) == int(game_1[2]):
    draw += 1

if int(game_2[0]) > int(game_2[2]):
    won += 1
elif int(game_2[0]) < int(game_2[2]):
    lost += 1
elif int(game_2[0]) == int(game_2[2]):
    draw += 1

if int(game_3[0]) > int(game_3[2]):
    won += 1
elif int(game_3[0]) < int(game_3[2]):
    lost += 1
elif int(game_3[0]) == int(game_3[2]):
    draw += 1

print(f"Team won {won} games.")
print(f"Team lost {lost} games.")
print(f"Drawn games: {draw}")
