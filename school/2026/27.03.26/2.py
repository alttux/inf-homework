print('x', 'y', 'z', 'w', "|", 'F')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                f = (not x or y) and (y==(not z)) and (z or w)
                if f == 1:
                    print(x, y, z, w, "|", f)

#