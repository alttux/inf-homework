print('x y z w | F')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                f = ((not x) and (not y) and z and w) or (x and y and z and (not w)) or ((not x) and y and z and w)
                if f == True:
                    print(f'{x} {y} {z} {w} | {int(f)}')
