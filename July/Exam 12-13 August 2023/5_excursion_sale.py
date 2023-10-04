sea_vacations = int(input())
mounting_vacations = int(input())
total_vacations = sea_vacations + mounting_vacations
total_sum = 0

while True:
    vacation_type = input()
    if vacation_type == "Stop":
        print(f"Profit: {total_sum} leva.")
        break

    if vacation_type == "sea":
        if sea_vacations > 0:
            total_sum += 680
            sea_vacations -= 1
        else:
            continue
    elif vacation_type == "mountain":
        if mounting_vacations > 0:
            total_sum += 499
            mounting_vacations -= 1
        else:
            continue

    if sea_vacations == 0 and mounting_vacations == 0:
        print(f" Good job! Everything is sold." )
        print(f"Profit: {total_sum} leva.")
        break
