days = int(input())
total_amount_food = float(input())

total_food_eaten = 0
eaten_biscuits = 0
eaten_by_dog = 0
eaten_by_cat = 0
counter = 0

for i in range(1, days + 1):
    counter += 1
    dog_food_eaten = int(input())
    cat_food_eaten = int(input())

    if counter == 3:
        biscuit = (dog_food_eaten + cat_food_eaten) * 0.10
        eaten_biscuits += biscuit
        counter = 0
    else:
        biscuit = 0

    total_food_eaten += (dog_food_eaten + cat_food_eaten)
    eaten_by_dog += dog_food_eaten
    eaten_by_cat += cat_food_eaten

print(f"Total eaten biscuits: {round(eaten_biscuits)}gr.")
print(f"{total_food_eaten/total_amount_food * 100:.2f}% of the food has been eaten.")
print(f"{eaten_by_dog/total_food_eaten*100:.2f}% eaten from the dog.")
print(f"{eaten_by_cat/total_food_eaten*100:.2f}% eaten from the cat.")
