print("x y w z F1 F2")

for x in range(2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                f1 = (x==y) and (not(w) or z)
                f2 = not(not(x) or y) or (w == z)
                print(x, y, w, z, int(f1), '',  int(f2))