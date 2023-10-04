contract_duration = input()
contract_type = input()
mobile_data = input()
months_to_pay = int(input())
tax_for_month = 0

if contract_duration == "one":
    if contract_type == "Small":
        tax_for_month = 9.98
    elif contract_type == "Middle":
        tax_for_month = 18.99
    elif contract_type == "Large":
        tax_for_month = 25.98
    elif contract_type == "ExtraLarge":
        tax_for_month = 35.99

elif contract_duration == "two":
    if contract_type == "Small":
        tax_for_month = 8.58
    elif contract_type == "Middle":
        tax_for_month = 17.09
    elif contract_type == "Large":
        tax_for_month = 23.59
    elif contract_type == "ExtraLarge":
        tax_for_month = 31.79

if mobile_data == "yes":
    if tax_for_month <= 10.00:
        tax_for_month += 5.50
    elif 10 < tax_for_month <= 30.00:
        tax_for_month += 4.35
    elif tax_for_month > 30.00:
        tax_for_month += 3.85

total = tax_for_month * months_to_pay

if contract_duration == "two":
    total = (total * 96.25) / 100

print(f"{total:.2f} lv.")
