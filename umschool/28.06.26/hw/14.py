for x in range(2030, 1, -1):
    s = 6**260 + 6**160 + 6**60 - x
    c = 0
    while s > 0:
        if s % 6 == 0:
            c +=1
        s //= 6
    if c == 202:
        print(x)
        break