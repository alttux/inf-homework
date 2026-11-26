from itertools import product


for n, w in enumerate(product(sorted('ВЕНРА'), repeat=5), 1):
    w = ''.join(w)
    if w[0] != 'Н' and w.count('В') == 2: print(n, w)