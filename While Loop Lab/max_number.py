number = input()
max_num = -1000000000000000000000000000

while number != "Stop":
    num = int(number)

    if num > max_num:
        max_num = num
    number = input()

print(max_num)