for x in range(2030, 1, -1):
    s = 7**91 + 7**160 - x
    c = 0
    while s > 0:
        if s % 7 == 0:
            c += 1
        s //= 7
    if c == 70:
        print(x)
        break
# 2029