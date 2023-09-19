last_section = input()
first_section_rows = int(input())
seats_on_odd_row = int(input())
seats_on_even_row = seats_on_odd_row + 2
total_seats = 0

for section in range(ord("A"), ord(last_section) + 1):
    for row in range(1, first_section_rows + 1):

        if row % 2 == 0:
            for seat in range(ord("a"), 97 + seats_on_even_row):
                print(f"{chr(section)}{row}{chr(seat)}")
                total_seats += 1
        else:
            for seat in range(ord("a"), 97 + seats_on_odd_row):
                print(f"{chr(section)}{row}{chr(seat)}")
                total_seats += 1

    first_section_rows += 1
print(total_seats)
