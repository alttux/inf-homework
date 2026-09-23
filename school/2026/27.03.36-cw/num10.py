for a in range(2):
    for b in range(2):
        for c in range(2):
            f1 = (a <= (not b))
            f2 = ((not a) and c)
            f3 = (not b) <= c
            f4 = not((not b) <= c)
            f = (a <= (not b)) or ((not a) and c) or( not((not b) <= c))
            print(a, b, c, '|', int(f1), int(f2), int(f3), int(f4), "|", int(f))