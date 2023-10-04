n = int(input())
prev_sum = 0
max_diff = 0
same_value = True

for _ in range(n):
    num1 = int(input())
    num2 = int(input())
    current_sum = num1 + num2

    if prev_sum != 0 and current_sum != prev_sum:
        same_value = False
        diff = abs(current_sum - prev_sum)
        if diff > max_diff:
            max_diff = diff

    prev_sum = current_sum

if same_value:
    print(f"Yes, value={prev_sum}")
else:
    print(f"No, maxdiff={max_diff}")


