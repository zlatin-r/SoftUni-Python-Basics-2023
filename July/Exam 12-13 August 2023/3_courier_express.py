parcel_weight = float(input())
type_of_service = input()
distance = int(input())
standard_price = 0
express_price = 0

if type_of_service == "standard":
    if 1 > parcel_weight:
        standard_price = 0.03
    elif 1 <= parcel_weight < 10:
        standard_price = 0.05
    elif 10 <= parcel_weight < 40:
        standard_price = 0.10
    elif 40 <= parcel_weight < 90:
        standard_price = 0.15
    elif 90 <= parcel_weight < 150:
        standard_price = 0.20

elif type_of_service == "express":
    if 1 > parcel_weight:
        standard_price = 0.03
    elif 1 <= parcel_weight < 10:
        standard_price = 0.05
    elif 10 <= parcel_weight < 40:
        standard_price = 0.10
    elif 40 <= parcel_weight < 90:
        standard_price = 0.15
    elif 90 <= parcel_weight < 150:
        standard_price = 0.20
    if 1 > parcel_weight:
        express_price += 0.03 * 0.80
    elif 1 <= parcel_weight < 10:
        express_price += 0.05 * 0.40
    elif 10 <= parcel_weight < 40:
        express_price += 0.10 * 0.05
    elif 40 <= parcel_weight < 90:
        express_price += 0.15 * 0.02
    elif 90 <= parcel_weight < 150:
        express_price += 0.20 * 0.01
price_transport = distance * standard_price
extra_price = express_price * parcel_weight
total_extra = distance * extra_price
total_price = price_transport + total_extra
print(f"The delivery of your shipment with weight of {parcel_weight:.3f} kg. would cost {total_price:.2f} lv.")
