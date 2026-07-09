print('x y z w F')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if ((not(x) or y) and (y or z) and w) == 1:
                    print(x, y, z, w, 1)
# yzxw