steps = 0

while steps < 10_000:
    input_line = input()

    if input_line == "Going home":
        steps += int(input())
        break

    steps += int(input_line)

if steps >= 10_000:
    print("Goal reached! Good job!")
    print(f"{steps - 10_000} steps over the goal!")
else:
    print(f"{10_000 - steps} more steps to reach goal.")