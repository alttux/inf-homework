from itertools import product


c = 0
for w in product(sorted('ПАЛЬТО'), repeat=5):
    w = ''.join(w)
    if w.count('О') <= 2 and w[0] != 'О' and w[-1] != 'О' and 'ОЛ' not in w and 'ЛО' not in w:
        print(w)
        c+=1

print(c)