tournament = input()
wins = 0
losses = 0
total_games = 0

while tournament != "End of tournaments":
    games_played = int(input())
    total_games += games_played

    for i in range(1, games_played + 1):
        Desi_team = int(input())
        opposing_team = int(input())

        if Desi_team > opposing_team:
            wins += 1
            print(f"Game {i} of tournament {tournament}: win with {Desi_team - opposing_team} points.")
        elif Desi_team < opposing_team:
            losses += 1
            print(f"Game {i} of tournament {tournament}: lost with {opposing_team - Desi_team} points.")

    tournament = input()

print(f"{wins / total_games * 100:.2f}% matches win")
print(f"{losses / total_games * 100:.2f}% matches lost")
