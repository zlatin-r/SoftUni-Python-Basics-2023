n = int(input())

max_odd_number = float('inf')
min_odd_number = float('-inf')

max_even_number = float('inf')
min_even_number = float('-inf')

odd_sum = 0
even_sum = 0
odd_min = 0
odd_max = 0
even_min = 0
even_max = 0

for i in range(1, n + 1):
    num = float(input())
    if i % 2 == 1:
        odd_sum += num
        if num > min_odd_number:
            min_odd_number = num
            odd_max = min_odd_number
            if odd_max < 0:
                odd_max = "NO"
        elif num < max_odd_number:
            max_odd_number = num
            odd_min = max_odd_number
            if odd_min < 0:
                odd_min = "NO"

    else:
        even_sum += num
        if num > min_even_number:
            min_even_number = num
            even_max = min_even_number
            if even_max < 0:
                even_max = "NO"
        elif num < max_even_number:
            max_even_number = num
            even_min = max_even_number
            if even_min < 0:
                even_min = "NO"


print(f"Odd sum: {odd_sum}")
print(f"Odd min: {odd_min}")
print(f"Odd max: {odd_max}")
print(f"Even sum: {even_sum}")
print(f"Even min: {even_min}")
print(f"Even max: {even_max}")
