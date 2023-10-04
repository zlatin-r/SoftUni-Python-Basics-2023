destination = input()
reservation_date = input()
overnight_stays = int(input())
price = 0

if destination == "France":
    if reservation_date == "21-23":
        price = 30 * overnight_stays
    elif reservation_date == "24-27":
        price = 35 * overnight_stays
    elif reservation_date == "28-31":
        price = 40 * overnight_stays

if destination == "Italy":
    if reservation_date == "21-23":
        price = 28 * overnight_stays
    elif reservation_date == "24-27":
        price = 32 * overnight_stays
    elif reservation_date == "28-31":
        price = 39 * overnight_stays

if destination == "Germany":
    if reservation_date == "21-23":
        price = 32 * overnight_stays
    elif reservation_date == "24-27":
        price = 37 * overnight_stays
    elif reservation_date == "28-31":
        price = 43 * overnight_stays

print(f"Easter trip to {destination} : {price:.2f} leva.")