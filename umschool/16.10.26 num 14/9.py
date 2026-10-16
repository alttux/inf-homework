for x in range(1, 2031):
    s = 13**220 + 13**150 + 13**40 - x
    c = 0
    while s > 0:
        if s % 13 == 0:
            c+=1
        s//= 13
    if c == 181:
        print(x)