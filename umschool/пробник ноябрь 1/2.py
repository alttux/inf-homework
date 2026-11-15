print('x y w z | F')
for x in range(2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                f = (x <= y) and not(y==z) and (w or x)
                if f:
                    print(f'{x} {y} {w} {z} | {int(f)}')