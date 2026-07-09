from itertools import product, permutations

for i, s in enumerate(product(sorted('АПРЕЛЬ'), repeat=6), 1):
    # print(str(s), i)
    if i%2!=0 and s[0] not in ['А', 'Л'] and s.count('П')>=2:
        print(i)
        break