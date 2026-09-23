for x in range(2070, 1, -1):
    s = 7**230 + 7**130 + 7**30 -x
    c = 0
    while s > 0:
        if s % 7 == 0:
            c += 1
        s //= 7
    if c == 199:
        print(x)
        break