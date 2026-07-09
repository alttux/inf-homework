print('x y z w F')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if (not(x==z) and not(not(w) or (y and z))) == 1:
                    print(x, y, z, w, 1)
# yxwz