first_letter = input()
last_letter = input()
pass_letter = input()
counter = 0

for first in range(ord(first_letter), ord(last_letter) + 1):
    for second in range(ord(first_letter), ord(last_letter) + 1):
        for third in range(ord(first_letter), ord(last_letter) + 1):

            if chr(first) != pass_letter and chr(second) != pass_letter and chr(third) != pass_letter:
                counter += 1
                print(f"{chr(first)}{chr(second)}{chr(third)}", end=" ")

print(counter)

