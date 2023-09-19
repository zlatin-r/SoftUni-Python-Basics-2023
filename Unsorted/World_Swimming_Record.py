world_rec = float(input())
distance = float(input())
time_1m = float(input())

delay = (distance//15)*12.5

Ivan_time = distance * time_1m + delay

if Ivan_time < world_rec:
    print(f'Yes, he succeeded! The new world record is {Ivan_time:.2f} seconds.')
elif Ivan_time >= world_rec:
    print(f'No, he failed! He was {(Ivan_time-world_rec):.2f} seconds slower.')


