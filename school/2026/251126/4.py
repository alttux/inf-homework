from itertools import product


for n, w in enumerate(product(sorted('ПАКТ'), repeat=5), 1):
    w = ''.join(w)
    if w.count('П') == 2 and 'A' not in w and 'ТТ' not in w:
        print(n,w)