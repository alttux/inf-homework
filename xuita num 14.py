for x in range(1000, 0):
    c_8 = 0
    c_4 = 0
    r = 9**500 + 9**100 - x

    while r > 0:
        if r % 9 == 8:
            c_8 += 1
        elif r % 9 == 4:
            c_4 += 1
        r//=9

    if c_8 == 90 and c_4 == 2:
        print(x)
        break