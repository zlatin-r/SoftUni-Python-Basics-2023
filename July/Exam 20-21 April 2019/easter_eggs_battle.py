player_one_eggs = int(input())
player_two_eggs = int(input())

while True:
    command = input()

    if command == "one":
        player_two_eggs -= 1
        if player_two_eggs == 0:
            print(f"Player two is out of eggs. Player one has {player_one_eggs} eggs left.")
            break

    elif command == "two":
        player_one_eggs -= 1
        if player_one_eggs == 0:
            print(f"Player one is out of eggs. Player two has {player_two_eggs} eggs left.")
            break

    elif command == "End":
        print(f"Player one has {player_one_eggs} eggs left.")
        print(f"Player two has {player_two_eggs} eggs left.")
        break


