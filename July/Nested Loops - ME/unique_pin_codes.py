first_num_upper_limit = int(input())
second_num_upper_limit = int(input())
third_num_upper_limit = int(input())

for first in range(2, first_num_upper_limit + 1, 2):
    for second in range(2, second_num_upper_limit + 1):
        is_prime = True

        for i in range(2, second):
            if second % i == 0:
                is_prime = False
                break

        if is_prime:
            for third in range(2, third_num_upper_limit + 1, 2):
                print(f"{first} {second} {third}")
