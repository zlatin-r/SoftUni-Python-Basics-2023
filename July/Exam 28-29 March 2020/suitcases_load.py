storage_capacity = float(input())
total_luggage_volume = 0
counter = 0

while True:
    luggage_volume = input()

    if luggage_volume == "End":
        print("Congratulations! All suitcases are loaded!")
        break

    counter += 1
    luggage_v = float(luggage_volume)

    if counter == 3:
        luggage_v += luggage_v * 0.10

    if storage_capacity - luggage_v < 0:
        counter -= 1
        print("No more space!")
        break
    else:
        storage_capacity -= luggage_v

print(f"Statistic: {counter} suitcases loaded.")
