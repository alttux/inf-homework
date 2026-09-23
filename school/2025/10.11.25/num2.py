print("x y z w F")
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                a = (not w or y) and (x or z)
                b = (z == w) or (y and not x)
                f = not a or b
                if f == 0:
                    print(x, y, z, w, 0)