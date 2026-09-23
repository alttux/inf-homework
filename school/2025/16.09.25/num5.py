print('x y z w F')
f = 1
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if ((x or not(y)) and not(w==z) and w) == f :
                    print(x, y ,z, w, f)