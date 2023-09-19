number_guests = int(input())
price_ticket = float(input())
budget = float(input())

if 10 <= number_guests <= 15:
    price_ticket -= price_ticket * 0.15
elif 15 < number_guests <= 20:
    price_ticket -= price_ticket * 0.20
elif 20 < number_guests:
    price_ticket -= price_ticket * 0.25

cake_price = budget * 0.10
total_tickets_price = number_guests * price_ticket + cake_price

if budget >= total_tickets_price:
    print(f"It is party time! {budget - total_tickets_price:.2f} leva left.")
elif budget < total_tickets_price:
    print(f"No party! {total_tickets_price - budget:.2f} leva needed.")