visitors = int(input())
back, chest, legs, abs_mus, protein_shake, protein_bar, train, buy = 0, 0, 0, 0, 0, 0, 0, 0

for i in range(visitors):
    activity = input()

    if activity == "Back":
        back += 1
        train += 1
    elif activity == "Chest":
        chest += 1
        train += 1
    elif activity == "Legs":
        legs += 1
        train += 1
    elif activity == "Abs":
        abs_mus += 1
        train += 1
    elif activity == "Protein shake":
        protein_shake += 1
        buy += 1
    elif activity == "Protein bar":
        protein_bar += 1
        buy += 1

print(f"{back} - back")
print(f"{chest} - chest")
print(f"{legs} - legs")
print(f"{abs_mus} - abs")
print(f"{protein_shake} - protein shake")
print(f"{protein_bar} - protein bar")
print(f"{train / visitors * 100:.2f}% - work out")
print(f"{buy / visitors * 100:.2f}% - protein")
