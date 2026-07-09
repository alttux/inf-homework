print('x y w z | F')
for x in range(2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                f = not(y <= x) and  not(not(w) and z) and not(x and w)
                if f == 1:
                    print(x, y, w, z, '|', int(f))