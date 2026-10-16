for x in "0123456789ABCDE":
    s1 = f'ACA{x}A'
    s2 = f'BC{x}E'
    s = int(s1, 15) + int(s2, 17)
    if s % 13 == 0:
        print(int(x, 15), s//13)
