from itertools import product


for n, w in enumerate(product(sorted('КРЕСТ'), repeat=5), 1):
    w = ''.join(w)
    if n % 2 != 0 and w[0] not in 'ЕК' and w.count('С') == 3:
        print(n, w)