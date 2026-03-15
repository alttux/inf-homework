c=0

for i in open('9_8.csv'):
    a = sorted(map(int, i.split(',')))
    p = [x for x in a if a.count(x)>1]

    if (len(p)==0 and not(a[-1] > sum(a[:-1]))) or (not(len(p)==0) and a[-1] > sum(a[:-1])):
        c+=1
print(c)
2222