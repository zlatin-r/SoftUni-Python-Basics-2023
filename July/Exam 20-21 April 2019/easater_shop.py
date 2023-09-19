amount_eggs = int(input())
sold_eggs = 0

while True:
    command = input()

    if command == "Close":
        print(f"Store is closed!")
        print(f"{sold_eggs} eggs sold.")
        break

    elif command == "Buy":
        buy_eggs = int(input())
        sold_eggs += buy_eggs

        if buy_eggs > amount_eggs:
            print(f"Not enough eggs in store!")
            print(f"You can buy only {amount_eggs}.")
            break

        amount_eggs -= buy_eggs

    elif command == "Fill":
        amount_eggs += int(input())
