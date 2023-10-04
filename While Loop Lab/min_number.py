number = input()
min_num = 1000000000000000000000000000

while number != "Stop":
    num = int(number)

    if num < min_num:
        min_num = num
    number = input()

print(min_num)