import math

kozunaks = int(input())
max_sugar = -99999
max_flour = -99999
total_sugar = 0
total_flour = 0

for i in range(kozunaks):
    sugar = int(input())
    flour = int(input())

    if sugar > max_sugar:
        max_sugar = sugar
    if flour > max_flour:
        max_flour = flour

    total_sugar += sugar
    total_flour += flour

print(f"Sugar: {math.ceil(total_sugar/950)}")
print(f"Flour: {math.ceil(total_flour/750)}")
print(f"Max used flour is {max_flour} grams, max used sugar is {max_sugar} grams.")
