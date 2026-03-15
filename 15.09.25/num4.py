print('x y z w F')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if ((not(x and y) or not(z)) and (not(x) or y) or w) == 0:
                    print(x, y, z, w, 0)
# xzwy