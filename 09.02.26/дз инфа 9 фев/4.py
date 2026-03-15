c=0

for i in open('9_4.csv'):
    a = sorted(map(int, i.split(',')))
    p = [x for x in a if a.count(x)>1]

    if len(p)==0:
        if 5*(a[0]+a[-1])>=3*(sum(a[1:-1])):
            c+=1
print(c)
3333