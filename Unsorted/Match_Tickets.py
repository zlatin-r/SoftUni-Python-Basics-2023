budget = float(input())
ticket_category = input()
count_people = int(input())

vip_tickets = 499.99
normal_tickets = 249.99
transport_budget = 0
ticket_price = 0

if 1 <= count_people <= 4:
    transport_budget = budget * 0.75
if 5 <= count_people <= 9:
    transport_budget = budget * 0.60
if 10 <= count_people <= 24:
    transport_budget = budget * 0.50
if 25 <= count_people <= 49:
    transport_budget = budget * 0.40
if 50 <= count_people:
    transport_budget = budget * 0.25

if ticket_category == "VIP":
    ticket_price = count_people * vip_tickets
if ticket_category == "Normal":
    ticket_price = count_people * normal_tickets

if budget >= (ticket_price + transport_budget):
    print(f"Yes! You have {abs(budget - (ticket_price + transport_budget)):.2f} leva left.")
else:
    print(f"Not enough money! You need {abs(budget-(ticket_price + transport_budget)):.2f} leva.")
