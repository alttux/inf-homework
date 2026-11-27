print('x y w z | F')

for x in range(2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                f = (x <= (y == w)) or (z and (not y))
                if not f:
                    print(f'{x} {y} {w} {z} | {int(f)}')


