from itertools import  product


alph = sorted('ЛИМОНР')

for i, n in enumerate(product(alph, repeat=5), 1):
    n = ''.join(n)
    if i % 2 == 0 and n[0] != 'И' and n[0] != 'Л' and n.count('О') >= 2:
        print(n , i)