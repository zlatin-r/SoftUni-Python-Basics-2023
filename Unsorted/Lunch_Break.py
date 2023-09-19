from math import ceil

name_of_series = input()
episode_time = float(input())
break_time = float(input())

lunch_time = break_time * 1 / 8
rest_time = break_time * 1 / 4

if episode_time <= break_time - (lunch_time + rest_time):
    print(f'You have enough time to watch {name_of_series} and left with \
{ceil(break_time - (episode_time + lunch_time + rest_time))} minutes free time.')
if episode_time > break_time - (lunch_time + rest_time):
    print(f"You don't have enough time to watch {name_of_series}, you need \
{ceil(abs(break_time - (episode_time + lunch_time + rest_time)))} more minutes.")
