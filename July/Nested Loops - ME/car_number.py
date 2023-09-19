start_num = int(input())
end_num = int(input())

for first in range(start_num, end_num + 1):
    for second in range(start_num, end_num + 1):
        for third in range(start_num, end_num + 1):
            for fourth in range(start_num, end_num + 1):

                if ((first % 2 == 0 and fourth % 2 == 1) or (first % 2 == 1 and fourth % 2 == 0)) and (
                        first > fourth) and (second + third) % 2 == 0:

                    print(f"{first}{second}{third}{fourth}", end=" ")
