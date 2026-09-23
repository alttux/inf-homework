for x in range(5030, 0, -1):
    s = 6**260 + 6**160 + 6**60 - x
    c_2 = 0
    c_3 = 0
    while s > 0:
        if s % 6 == 2:
            c_2 += 1
        elif s % 6 == 3:
            c_3 += 1
        s //= 6
    if c_2 == c_3:
        print(x)
        break
