country = input()
discipline = input()
difficulty = 0
performance = 0

if country == "Russia":
    if discipline == "ribbon":
        difficulty = 9.100
        performance = 9.400
    elif discipline == "hoop":
        difficulty = 9.300
        performance = 9.800
    elif discipline == "rope":
        difficulty = 9.600
        performance = 9.000
elif country == "Bulgaria":
    if discipline == "ribbon":
        difficulty = 9.600
        performance = 9.400
    elif discipline == "hoop":
        difficulty = 9.550
        performance = 9.750
    elif discipline == "rope":
        difficulty = 9.500
        performance = 9.400
elif country == "Italy":
    if discipline == "ribbon":
        difficulty = 9.200
        performance = 9.500
    elif discipline == "hoop":
        difficulty = 9.450
        performance = 9.350
    elif discipline == "rope":
        difficulty = 9.700
        performance = 9.150

total_points = difficulty + performance
per_needed = (20 - total_points) / 20 * 100

print(f"The team of {country} get {total_points:.3f} on {discipline}.")
print(f"{per_needed:.2f}%")
