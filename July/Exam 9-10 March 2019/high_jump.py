high = int(input())
starting_high = high - 30
fails = 0
jumps = 0

while starting_high < high or starting_high == high:
    jumps += 1
    jump = int(input())

    if jump > starting_high:
        starting_high += 5
        fails = 0
    else:
        fails += 1

    if fails == 3:
        break

if fails == 3:
    print(f"Tihomir failed at {starting_high}cm after {jumps} jumps.")
else:
    print(f"Tihomir succeeded, he jumped over {high}cm after {jumps} jumps.")
