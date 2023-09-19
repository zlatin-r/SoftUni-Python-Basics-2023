min_control = int(input())
sec_control = int(input())
distance = float(input())
sec_per_100m = int(input())

delay = (distance / 120) * 2.5
total_control_secs = min_control * 60 + sec_control
marins_time = (distance / 100) * sec_per_100m - delay

if marins_time <= total_control_secs:
    print("Marin Bangiev won an Olympic quota!")
    print(f"His time is {marins_time:.3f}.")
else:
    print(f"No, Marin failed! He was {marins_time - total_control_secs:.3f} second slower.")
