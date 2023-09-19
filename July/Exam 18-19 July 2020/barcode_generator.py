start = input()
end = input()

first_digit_start = int(start[0])
second_digit_start = int(start[1])
third_digit_start = int(start[2])
forth_digit_start = int(start[3])

first_digit_end = int(end[0])
second_digit_end = int(end[1])
third_digit_end = int(end[2])
forth_digit_end = int(end[3])

for i in range(first_digit_start, first_digit_end + 1):
    for k in range(second_digit_start, second_digit_end + 1):
        for m in range(third_digit_start, third_digit_end + 1):
            for n in range(forth_digit_start, forth_digit_end + 1):

                if i % 2 == 0 or k % 2 == 0 or m % 2 == 0 or n % 2 == 0:
                    pass
                else:
                    print(f"{i}{k}{m}{n}", end=" ")
