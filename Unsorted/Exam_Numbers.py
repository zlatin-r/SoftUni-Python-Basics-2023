x = int(input())
y = int(input())
t = int(input())

for i in range(x, y+1):
    digits = [int(d) for d in str(i)]
    if sum(digits) == t:
        print(i)