from itertools import product
k=0
for c in product('ИВАН', repeat=5):
    if 'И' in c:
        k+=1

print(k)
