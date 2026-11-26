from itertools import product


c = 0
for n, w in enumerate(product(sorted('ТЕРМИНЫ'), repeat=5), 1):
    w = ''.join(w)
    if n % 2 != 0 and w[0] != 'Р' and 1 <= w.count('М') <= 2: print(w); c+=1

print(c)
