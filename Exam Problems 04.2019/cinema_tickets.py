student = 0
standard = 0
kid = 0
total_tickets = 0

while True:
    movie_name = input()
    if movie_name == "Finish":
        break

    count = 0
    free_seats = int(input())

    while True:
        if count >= free_seats:
            break

        ticket = input()
        count += 1

        if ticket == "student":
            student += 1
        elif ticket == "standard":
            standard += 1
        elif ticket == "kid":
            kid += 1
        elif ticket == "End":
            count -= 1
            break

    total_tickets += count

    salon_full = (count / free_seats) * 100
    print(f"{movie_name} - {salon_full:.2f}% full.")

student_tickets = (student / total_tickets) * 100
standard_tickets = (standard / total_tickets) * 100
kid_tickets = (kid / total_tickets) * 100


print(f"Total tickets: {total_tickets}")
print(f"{student_tickets:.2f}% student tickets.")
print(f"{standard_tickets:.2f}% standard tickets.")
print(f"{kid_tickets:.2f}% kids tickets.")
