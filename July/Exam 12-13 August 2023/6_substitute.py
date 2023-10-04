K = int(input())
L = int(input())
M = int(input())
N = int(input())

count_changes = 0

for first_digit_p1 in range(K, 9):
    for second_digit_p1 in range(9, L - 1, -2):
        for first_digit_p2 in range(M, 9):
            for second_digit_p2 in range(9, N - 1, -2):

                player1 = f"{first_digit_p1}{second_digit_p1}"
                player2 = f"{first_digit_p2}{second_digit_p2}"

                if first_digit_p1 % 2 == 0 and first_digit_p2 % 2 == 0:
                    if second_digit_p1 % 2 == 1 and second_digit_p2 % 2 == 1:
                        if player1 != player2:
                            print(f"{player1} - {player2}")
                            count_changes += 1
                        else:
                            print("Cannot change the same player.")

                if count_changes == 6:
                    exit(0)
