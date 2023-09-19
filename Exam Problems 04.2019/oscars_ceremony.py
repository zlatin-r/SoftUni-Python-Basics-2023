rent = int(input())

statuettes = rent - (rent * 0.30)
kettering = statuettes - (statuettes * 0.15)
sound = kettering / 2

budget = rent + statuettes + kettering + sound

print(f"{budget:.2f}")
