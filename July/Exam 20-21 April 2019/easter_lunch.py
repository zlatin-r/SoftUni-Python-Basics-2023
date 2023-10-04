breads = int(input())
eggshells = int(input())
cookies_kilos = int(input())

price_breads = breads * 3.20
price_cookies = cookies_kilos * 5.40
price_eggs = eggshells * 4.35
price_paint = eggshells * 12 * 0.15

total_price = price_breads + price_cookies + price_eggs + price_paint

print(f"{total_price:.2f}")
