from math import floor

tournaments = int(input())
starting_points = int(input())
points_win = 0
tournaments_wins = 0

for _ in range(tournaments):
    result = input()

    if result == "W":
        starting_points += 2000
        points_win += 2000
        tournaments_wins += 1
    elif result == "F":
        starting_points += 1200
        points_win += 1200
    elif result == "SF":
        starting_points += 720
        points_win += 720

print(f"Final points: {starting_points}")
print(f"Average points: {floor(points_win / tournaments)}")
print(f"{tournaments_wins / tournaments * 100:.2f}%")
