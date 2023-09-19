bad_grades = int(input())
counter_bad_grades = 0
counter_grades = 0
average_counter = 0
last_task = ""

while True:
    task_name = input()

    if task_name != "Enough":
        last_task = task_name

    if task_name == "Enough":
        print(f"Average score: {(average_counter / counter_grades):.2f}")
        print(f"Number of problems: {counter_grades}")
        print(f"Last problem: {last_task}")
        break

    grade = int(input())

    if grade <= 4:
        counter_bad_grades += 1

    if bad_grades == counter_bad_grades:
        print(f"You need a break, {counter_bad_grades} poor grades.")
        break

    average_counter += grade
    counter_grades += 1
