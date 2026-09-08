from itertools import*
cnt1 = 0
cnt2 = 0
for i in product('НЧ', repeat = 12):
    p = ''.join(i)
    if p[0]=='Н' and p.count('Н')==3 and p.count('НН')==0:
        cnt1 += 1
    elif p[0]=='Ч' and p.count('Н')==3 and p.count('НН')==0:
        cnt2 += 1
print(4**12*cnt1 + 3*4**11*cnt2)