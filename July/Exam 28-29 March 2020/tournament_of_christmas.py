days = int(input())  # Брой дни на турнира
total_money = 0  # Общо спечелени пари

total_wins = 0  # Общо спечелени игри
total_losses = 0  # Общо загубени игри

for day in range(1, days + 1):
    daily_money = 0  # Пари за текущия ден
    daily_wins = 0  # Спечелени игри за текущия ден
    daily_losses = 0  # Загубени игри за текущия ден

    while True:
        game_result = input()

        if game_result == "Finish":
            break

        if game_result == "win":
            daily_money += 20
            daily_wins += 1
        elif game_result == "lose":
            daily_losses += 1

    if daily_wins > daily_losses:
        daily_money *= 1.10

    total_money += daily_money
    total_wins += daily_wins
    total_losses += daily_losses

if total_wins > total_losses:
    total_money *= 1.20
    print(f"You won the tournament! Total raised money: {total_money:.2f}")
else:
    print(f"You lost the tournament! Total raised money: {total_money:.2f}")
