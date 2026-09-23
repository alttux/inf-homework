print('w x y z | F')
for w in range(2):
    for x in range(2):
        for y in range(2):
            for z in range(2):
                f = (not(w == (not x)) or not((not y) or w)) or (not z)
                if not f:
                    print(w, x, y, z, '|', int(f))