print("x y z w F")
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if ((w <= (y==z)) and (y == (z <= x))) == 1:
                    print(x, y, z, w, 1)
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if ((w <= (y==z)) and (y == (z <= x))) == 0:
                    print(x, y, z, w, 0)