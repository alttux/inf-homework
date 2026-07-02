s =  3 * 289**2024 + 81 * 49**121 - 9 * 16**81 - 6011
summa = 0
while s > 0:
    num = s % 31
    if num <= 17:
        summa += num
    s//=31

print(summa)

# 16750