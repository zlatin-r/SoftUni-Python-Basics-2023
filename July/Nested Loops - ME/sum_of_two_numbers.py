start_index = int(input())
end_index = int(input())
magic_number = int(input())
result = ""
count = 0
flag = False

for i in range(start_index, end_index + 1):
    for j in range(start_index, end_index + 1):
        count += 1

        if i + j == magic_number:
            result = f"Combination N:{count} ({i} + {j} = {magic_number})"

            flag = True
            break
    if flag:
        break
    else:
        result = f"{count} combinations - neither equals {magic_number}"
print(result)
