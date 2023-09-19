first = int(input())
second = int(input())
diff_first = int(input())
diff_second = int(input())

end_first = first + diff_first
end_second = second + diff_second

for num1 in range(first, end_first + 1):
    is_prime = True
    for a in range(2, num1):
        if num1 % a == 0:
            is_prime = False

    for num2 in range(second, end_second + 1):
        is_prime2 = True
        for b in range(2, num2):
            if num2 % b == 0:
                is_prime2 = False

        if is_prime and is_prime2:
            print(f"{num1}{num2}")
