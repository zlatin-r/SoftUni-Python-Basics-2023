count_junior_bikers = int(input())
count_senior_bikers = int(input())
type_route = input()

sum_fee = 0

if type_route == "trail":
    sum_fee = count_junior_bikers * 5.50 + count_senior_bikers * 7
elif type_route == "cross-country":
    sum_fee = count_junior_bikers * 8 + count_senior_bikers * 9.50
    if count_junior_bikers + count_senior_bikers >= 50:
        sum_fee *= 0.75
elif type_route == "downhill":
    sum_fee = count_junior_bikers * 12.25 + count_senior_bikers * 13.75
elif type_route == "road":
    sum_fee = count_junior_bikers * 20 + count_senior_bikers * 21.50

sum_fee *= 0.95

print(f"{sum_fee:.2f}")
