room_rent = int(input())

cake = room_rent * 0.20
drinks = cake - (cake * 0.45)
animator = room_rent / 3

needed_budget = room_rent + cake + drinks + animator

print(needed_budget)
