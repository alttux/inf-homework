print('x y z w F')
f = 0
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if ((x and not(y)) or (x==z) or not(w)) == f:
                    print(x, y ,z, w, f)