from math import ceil

days_train = int(input())
first_day = float(input())
total_km = 0
current_day = 0
sum_km = 0

for i in range(days_train + 1):
    if i == 0:
        total_km += first_day
        sum_km += total_km
        continue
    increase_percentage = int(input()) / 100
    current_day = total_km * increase_percentage
    total_km += current_day
    sum_km += total_km


if sum_km >= 1000:
    print(f"You've done a great job running {ceil(sum_km - 1000)} more kilometers!")
else:
    print(f"Sorry Mrs. Ivanova, you need to run {ceil(1000-sum_km)} more kilometers")
