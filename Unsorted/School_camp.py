season = input()
type_group = input()
students = int(input())
overnight_stays = int(input())

sports = ""
price = 0

if season == "Winter":
    if type_group == "girls":
        sports = "Gymnastics"
        price = (overnight_stays * 9.60) * students
    elif type_group == "boys":
        sports = "Judo"
        price = (overnight_stays * 9.60) * students
    elif type_group == "mixed":
        sports = "Ski"
        price = (overnight_stays * 10) * students

if season == "Summer":
    if type_group == "girls":
        sports = "Volleyball"
        price = (overnight_stays * 15) * students
    elif type_group == "boys":
        sports = "Football"
        price = (overnight_stays * 15) * students
    elif type_group == "mixed":
        sports = "Swimming"
        price = (overnight_stays * 20) * students

if season == "Spring":
    if type_group == "girls":
        sports = "Athletics"
        price = (overnight_stays * 7.20) * students
    elif type_group == "boys":
        sports = "Tennis"
        price = (overnight_stays * 7.20) * students
    elif type_group == "mixed":
        sports = "Cycling"
        price = (overnight_stays * 9.50) * students

if students >= 50:
    price *= 0.50
elif 20 <= students < 50:
    price *= 0.85
elif 10 <= students < 20:
    price *= 0.95

print(f"{sports} {price:.2f} lv.")