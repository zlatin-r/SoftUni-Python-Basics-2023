number_of_bottles = int(input())
total_detergent = number_of_bottles * 750
total_dishes = 0
total_pots = 0
counter = 0
line = ""

while total_detergent >= 0:
    counter += 1
    amount = input()

    if amount == "End":
        break

    if counter % 3 == 0:
        total_detergent -= int(amount) * 15
        total_pots += int(amount)
        counter = 0
    else:
        total_detergent -= int(amount) * 5
        total_dishes += int(amount)

if total_detergent >= 0:
    print("Detergent was enough!")
    print(f"{total_dishes} dishes and {total_pots} pots were washed.")
    print(f"Leftover detergent {total_detergent} ml.")
else:
    print(f"Not enough detergent, {abs(total_detergent)} ml. more necessary!")
