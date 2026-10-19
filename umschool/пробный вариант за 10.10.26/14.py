for x in range(1, 2501):
    s = 6**210 + 6**140 - x
    c = 0
    while s > 0:
        if s % 6 == 0:
            c+=1
        s//=6
    if c == 73:
        print(x)