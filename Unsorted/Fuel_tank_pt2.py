Gasoline = 2.22
Diesel = 2.33
Gas = 0.93
fuel_type = input()
fuel_quantity = float(input())
club_card = input()
fuel_price = 0
discount = 0

if club_card == "No":
    if fuel_quantity < 20:
        if fuel_type == "Gasoline":
            fuel_price = Gasoline * fuel_quantity
        elif fuel_type == "Diesel":
            fuel_price = Diesel * fuel_quantity
        elif fuel_type == "Gas":
            fuel_price = Gas * fuel_quantity
    if 25 >= fuel_quantity >= 20:
        if fuel_type == "Gasoline":
            fuel_price = Gasoline * fuel_quantity
            fuel_price *= 0.92
        elif fuel_type == "Diesel":
            fuel_price = Diesel * fuel_quantity
            fuel_price *= 0.92
        elif fuel_type == "Gas":
            fuel_price = Gas * fuel_quantity
            fuel_price *= 0.92
    if 25 < fuel_quantity:
        if fuel_type == "Gasoline":
            fuel_price = Gasoline * fuel_quantity
            fuel_price *= 0.90
        elif fuel_type == "Diesel":
            fuel_price = Diesel * fuel_quantity
            fuel_price *= 0.90
        elif fuel_type == "Gas":
            fuel_price = Gas * fuel_quantity
            fuel_price *= 0.90

if club_card == "Yes":
    if fuel_quantity < 20:
        if fuel_type == "Gasoline":
            discount = fuel_quantity * 0.18
            fuel_price = (Gasoline * fuel_quantity) - discount
        elif fuel_type == "Diesel":
            discount = fuel_quantity * 0.12
            fuel_price = (Diesel * fuel_quantity) - discount
        elif fuel_type == "Gas":
            discount = fuel_quantity * 0.08
            fuel_price = (Gas * fuel_quantity) - discount
    if 25 >= fuel_quantity >= 20:
        if fuel_type == "Gasoline":
            discount = fuel_quantity * 0.18
            fuel_price = (Gasoline * fuel_quantity) - discount
            fuel_price *= 0.92
        elif fuel_type == "Diesel":
            discount = fuel_quantity * 0.12
            fuel_price = (Diesel * fuel_quantity) - discount
            fuel_price *= 0.92
        elif fuel_type == "Gas":
            discount = fuel_quantity * 0.08
            fuel_price = (Gas * fuel_quantity) - discount
            fuel_price *= 0.92
    if 25 < fuel_quantity:
        if fuel_type == "Gasoline":
            discount = fuel_quantity * 0.18
            fuel_price = (Gasoline * fuel_quantity) - discount
            fuel_price *= 0.90
        elif fuel_type == "Diesel":
            discount = fuel_quantity * 0.12
            fuel_price = (Diesel * fuel_quantity) - discount
            fuel_price *= 0.90
        elif fuel_type == "Gas":
            discount = fuel_quantity * 0.08
            fuel_price = (Gas * fuel_quantity) - discount
            fuel_price *= 0.90

print(f"{fuel_price:.2f} lv.")
