from itertools import product


c = 0
for w in product(sorted('ЧКИБАМОНЩЕ'), repeat=6):
    w = ''.join(w)
    if sum([w.count(x) for x in 'ИАОЕ']) > sum([w.count(x) for x in 'ЧКБМНЩ']) and w.count('Щ') == 1 and w[0] in 'ИАОЕ':
        c+=1

print(c)