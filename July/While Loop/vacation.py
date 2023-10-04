vacation_cost = float(input())
budget = float(input())
days_count = 0
days_spend = 0
flag = False

while budget < vacation_cost:
    spend_or_save = input()
    amount = float(input())
    days_count += 1

    if spend_or_save == 'spend':
        days_spend += 1
        budget -= amount

        if days_spend == 5:
            flag = True
            break

        if budget < 0:
            budget = 0

    elif spend_or_save == 'save':
        days_spend = 0
        budget += amount

if flag:
    print(f"You can't save the money.")
    print(days_count)
else:
    print(f"You saved the money for {days_count} days.")