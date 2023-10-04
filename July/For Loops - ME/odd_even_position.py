count = int(input())
oddSum = 0
evenSum = 0

if count == 0:
    print(f"OddSum={oddSum:.2f},\nOddMin=No,\nOddMax=No,\nEvenSum={evenSum:.2f},\nEvenMin=No,\nEvenMax=No")
elif count == 1:
    first = float(input())
    print(f"OddSum={first:.2f},\nOddMin={first:.2f},\nOddMax={first:.2f},\nEvenSum={evenSum:.2f},\nEvenMin=No,\nEvenMax=No")
else:
    first = float(input())
    oddMin = first
    oddMax = first
    oddSum += first

    second = float(input())
    evenMin = second
    evenMax = second
    evenSum += second

    for i in range(count - 2):
        current = float(input())
        if i % 2 == 0:
            oddSum += current
            if current > oddMax:
                oddMax = current
            if current < oddMin:
                oddMin = current
        else:
            evenSum += current
            if current > evenMax:
                evenMax = current
            if current < evenMin:
                evenMin = current

    print(f"OddSum={oddSum:.2f},\nOddMin={oddMin:.2f},\nOddMax={oddMax:.2f},\nEvenSum={evenSum:.2f},\nEvenMin={evenMin:.2f},\nEvenMax={evenMax:.2f}")