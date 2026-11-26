from itertools import permutations
print(len([''.join(w) for w in set(permutations(sorted('ЖАННА'), r=5)) if all(f'{x}{x}' not in ''.join(w) for x in [y for y in w if w.count(y) > 1])]))
