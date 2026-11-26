from itertools import product


for n, w in enumerate(product(sorted('КАПУСТ'), repeat=6), 1):
    w = ''.join(w)
    if n % 2 == 0 and w[0] != 'А' and 'П' not in w and w.count('У') == 1 and w.count("С") == 1:
        print(n, w)