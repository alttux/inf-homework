import math
c=0

for i in open('9_7.csv'):
    a = sorted(map(int, i.split(',')))
    p = [x for x in a if a.count(x)>1]

    if a[-1]**2 > math.prod(a[:-1]):
        if a[-1]+a[-2] > 2*sum(a[:-2]):
            c+=1
print(c)
10