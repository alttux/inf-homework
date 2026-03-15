c=0

for i in open('9_10.csv'):
    a = sorted(map(int, i.split(',')))
    p = [x for x in a if a.count(x)>1]
    if len(p)==0:
        if sum(a)%3==0:
            c+=1
print(c)
610