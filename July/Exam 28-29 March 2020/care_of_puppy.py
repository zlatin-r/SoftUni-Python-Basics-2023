food_amount = int(input()) * 1000
food_eaten = 0

while True:
    line = input()

    if line == "Adopted":
        if food_amount < 0:
            print(f"Food is not enough. You need {abs(food_amount)} grams more.")
            break
        else:
            print(f"Food is enough! Leftovers: {food_amount} grams.")
            break

    food_eaten = int(line)
    food_amount -= food_eaten
