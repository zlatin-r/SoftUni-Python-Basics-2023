from math import floor

record_in_secs = float(input())
distance_in_meters = float(input())
time_for_meter_in_secs = float(input())

total_time = distance_in_meters * time_for_meter_in_secs
extra_time = distance_in_meters / 50
round_time = floor(extra_time)
total_extra_time = round_time * 30
total = total_extra_time + total_time

if total < record_in_secs:
    print(f"Yes! The new record is {total:.2f} seconds.")
else:
    print(f"No! He was {abs(record_in_secs - total):.2f} seconds slower.")

