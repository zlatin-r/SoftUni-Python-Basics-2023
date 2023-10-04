min_walk_per_day = int(input())
walks_pre_day = int(input())
calories_per_day = int(input())

total_min_per_day = walks_pre_day * min_walk_per_day
total_burned_calories = total_min_per_day * 5
needed_to_burn = calories_per_day / 2

if total_burned_calories >= needed_to_burn:
    print(f"Yes, the walk for your cat is enough. Burned calories per day: {total_burned_calories}.")
else:
    print(f"No, the walk for your cat is not enough. Burned calories per day: {total_burned_calories}.")
