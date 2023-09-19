students = int(input())
top = 0
good = 0
not_good = 0
fail = 0
total_grades = 0

for i in range(1, students + 1):
    grade = float(input())
    total_grades += grade

    if grade < 3:
        fail += 1
    elif 3 <= grade < 4:
        not_good += 1
    elif 4 <= grade < 5:
        good += 1
    else:
        top += 1

print(f"Top students: {(top / students) * 100:.2f}%")
print(f"Between 4.00 and 4.99: {(good / students) * 100:.2f}%")
print(f"Between 3.00 and 3.99: {(not_good / students) * 100:.2f}%")
print(f"Fail: {(fail / students) * 100:.2f}%")
print(f"Average: {total_grades / students:.2f}")

