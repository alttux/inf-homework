print('x y z w F')
f = 1
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if (((not(y) or z) or (not(x) and w)) == (w==z)) == 1 :
                    print(x, y ,z, w, f)