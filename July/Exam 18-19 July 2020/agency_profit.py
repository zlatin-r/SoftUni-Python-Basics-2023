agency_name = input()
adult_tickets = int(input())
children_tickets = int(input())
net_price_adults = float(input())
service_charge = float(input())

net_price_children = net_price_adults * 0.30
price_adults = net_price_adults + service_charge
price_children = net_price_children + service_charge

total_tickets_price = (adult_tickets * price_adults) + (children_tickets * price_children)

profit = total_tickets_price * 0.20

print(f"The profit of your agency from {agency_name} tickets is {profit:.2f} lv.")