print('x y w z | F')
for x in range(2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                f = (not(x) and z and not(y) and not(w)) or (not(x) and z and y and not(w)) or (not(x) and z and y and w)
                if f == 1:
                    print(x, y, w, z, '|', int(f))
