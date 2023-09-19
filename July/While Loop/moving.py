width = int(input())
length = int(input())
height = int(input())
free_space = width * height * length
flag = False

while free_space > 0:
    line_input = input()

    if line_input == "Done":
        flag = True
        break
    else:
        free_space -= int(line_input)

if flag:
    print(f"{free_space} Cubic meters left.")
else:
    print(f"No more free space! You need {abs(free_space)} Cubic meters more.")