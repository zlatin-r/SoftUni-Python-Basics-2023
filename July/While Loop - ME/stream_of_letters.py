secret_command = "con"
alphabet = "ABCDEFGHIJKLMNOPQRSTUabcdefghijklmnopqrstuvwxyz"
seen = ""
result = ""

while seen != secret_command:
    letter = input()

    if letter == "End":
        break

    if letter in alphabet:
        if letter in secret_command:
            if letter not in seen:
                seen += letter

                if len(seen) == 3:
                    print(result, end=" ")
                    seen = ""
                    result = ""
            else:
                result += letter
        else:
            result += letter
    else:
        continue

