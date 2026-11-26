from itertools import permutations


c = 0
for w in permutations(sorted('БАЛДЁЖ'), r=6):
    w = ''.join(w)
    if 'АЁ' not in w and 'ЁА' not in w:
        c+=1

print(c)