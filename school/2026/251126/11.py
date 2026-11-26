from itertools import product


c = 0
for n in product(sorted('012345678'), repeat=6):
    n = ''.join(n)
    if n[0] not in '13570' and n[-1] not in '25' and n.count('1') >= 2:
        c+=1

print(c)