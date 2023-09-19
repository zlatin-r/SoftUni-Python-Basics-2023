men_customers = int(input())
female_customers = int(input())
max_num_tables = int(input())

for men in range(1, men_customers + 1):
    for female in range(1, female_customers + 1):

        if max_num_tables == 0:
            break

        print(f"({men} <-> {female})", end=" ")
        max_num_tables -= 1

