from itertools import product


c = 0
for n, w in enumerate(product(sorted('КОЛБА'), repeat=5), 1):
    w = ''.join(w)
    if n % 2 == 0 and w[0] != 'О' and w.count('А') in [1, 2]:
        print(n, w)
        c+=1

print(c)