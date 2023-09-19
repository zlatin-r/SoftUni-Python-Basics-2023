n = int(input())
m = int(input())

for i in range(1, n + 1):
    for j in range(1, n + 1):
        for k in range(97, 97 + m):
            for o in range(97, 97 + m):
                for p in range(1, n + 1):

                    if p > i and p > j:
                        print(f"{i}{j}{chr(k)}{chr(o)}{p}", end=" ")

