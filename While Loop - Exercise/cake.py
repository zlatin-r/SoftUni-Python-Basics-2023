N = input()

sum_digits = 0


while sum_digits < 9:
    for i in range(len(N)):
        sum_digits += i
    print(sum_digits)



