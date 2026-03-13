for x in range(2031):
    s = 3 ** 100 - x
    c = 0
    while s > 0:
        if s % 3 == 0:
            c += 1
        s //= 3
    if c == 5:
        print(x)
