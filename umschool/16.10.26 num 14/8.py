for x in range(1, 3001):
    s = 3 * 17**230 + 13 * 17**180 - x
    c = 0
    while s > 0:
        if s % 17 == 0:
            c+=1
        s//=17
    if c == 50:
        print(x)