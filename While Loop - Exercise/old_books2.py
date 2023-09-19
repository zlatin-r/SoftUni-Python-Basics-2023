searched_book = input()
counter = 0

while True:
    checked_book = input()

    if checked_book == searched_book:
        print(f"You checked {counter} books and found it.")
        break
    elif checked_book == "No More Books":
        print("The book you search is not here!")
        print(f"You checked {counter} books.")
        break
    counter += 1
