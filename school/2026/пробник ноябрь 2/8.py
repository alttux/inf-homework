from itertools import product


c = 0
for n in product('01234567', repeat=5):
    n = ''.join(n)
    if n.count('3') == 1 and n.count('6') <= 2:
        c+=1

print(c)