inherited_money = float(input())
year_to_live = int(input()) - 1800
ivan_age = 18

for i in range(year_to_live + 1):
    if i % 2 == 0:
        inherited_money -= 12000
    else:
        inherited_money -= 12000 + (ivan_age * 50)
    ivan_age += 1
if inherited_money < 0:
    print(f"He will need {abs(inherited_money):.2f} dollars to survive.")
else:
    print(f"Yes! He will live a carefree life and will have {inherited_money:.2f} dollars left.")
