n = int(input())

min_value = -1000000000.0
max_value = 1000000000.0

OddSum = 0
OddMin = 0
OddMax = 0
EvenSum = 0
EvenMin = 0
EvenMax = 0

for i in range(1, n + 1):
    number = float(input())
    if i % 2 == 1:
        OddSum += number
        if number < max_value:     # odd min value
            max_value = number
