p1_name = input()
p2_name = input()
p1_points = 0
p2_points = 0

while True:
    p1_card = input()

    if p1_card == "End of game":
        print(f"{p1_name} has {p1_points} points")
        print(f"{p2_name} has {p2_points} points")
        break
    else:
        p1_card_points = int(p1_card)

    p2_card = input()
    if p2_card == "End of game":
        print(f"{p1_name} has {p1_points} points")
        print(f"{p2_name} has {p2_points} points")
        break
    else:
        p2_card_points = int(p2_card)

    if p1_card_points > p2_card_points:
        p1_points += p1_card_points - p2_card_points
    elif p2_card_points > p1_card_points:
        p2_points += p2_card_points - p1_card_points
    else:
        print("Number wars!")
        p1_card = input()
        p2_card = input()

        if int(p1_card) > int(p2_card):
            print(f"{p1_name} is winner with {p1_points} points")
            break
        elif int(p2_card) > int(p1_card):
            print(f"{p2_name} is winner with {p2_points} points")
            break
