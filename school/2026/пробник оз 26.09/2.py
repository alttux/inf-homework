from itertools import product, permutations

def f(x, y, z, w):
    return (w == y) or ((x or not y) and (z or x))

for p in permutations('xyzw'):
    for a in product([0, 1], repeat=3):
        t = [(0, a[0], 1, 1), (0, 0, 0, 1), (1, 0, a[1], a[2])]
        if len(t) == len(set(t)) and all(f(**dict(zip(p, r))) == 0 for r in t):
            print("".join(p))