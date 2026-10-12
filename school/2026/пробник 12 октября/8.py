from itertools import product
alf='ИРСТУЦ'; last=i=0
for w in product(alf,repeat=5):
    i+=1; s=''.join(w)
    if s.count('И')==2 and 'ЦЦ' not in s: last=i
print(last)