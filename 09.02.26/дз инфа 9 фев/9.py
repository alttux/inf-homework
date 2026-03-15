c=0

for i in open('9_9.csv'):
    a = sorted(map(int, i.split(',')))
    p = [x for x in a if a.count(x)>1]

    if 2*(a[0])**2 > a[1]*a[2]:
        if len(p)>0:
            c+=1
print(c)
56