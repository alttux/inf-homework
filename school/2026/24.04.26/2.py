print('x y w z | F')
for x in range(2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                f = ((not(w) and z and not(y) and not(x)) or (not(w) and z and y and not(x)) or (not(w) and z and y and x))
                if f:
                    print(x, y, w, z, '|', int(f))
