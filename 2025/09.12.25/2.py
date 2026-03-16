print("x y z w F1 F2")
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F1 = (w == x) and (not (y) or z)
                F2 = not (not (w) or x) or (y == z)
                print(x, y, z, w, int(F1), int(F2))
