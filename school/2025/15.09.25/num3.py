print('x y z w F')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if (not(x and y) and (z or not(x)) or w) == 0:
                    print(x, y, z, w, 0)
# ywzx