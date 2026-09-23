s = 9 ** 8 + 3 ** 24 - 3 * 7
c = 0
while s > 0:
    if s % 3 == 2:
        c += 1
    s //= 3
print(c)
