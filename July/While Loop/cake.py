length = int(input())
width = int(input())
cake_size = length * width
flag = False

while cake_size > 0:
    line_input = input()

    if line_input == "STOP":
        flag = True
        break
    else:
        taken_pieces = int(line_input)
        cake_size -= taken_pieces

if flag:
    print(f"{cake_size} pieces are left.")
else:
    print(f"No more cake left! You need {abs(cake_size)} pieces more.")
