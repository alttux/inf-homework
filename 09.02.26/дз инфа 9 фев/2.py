c=0

for i in open('9_2.csv'):
    a = list(map(int, i.split(',')))
    p = [x for x in a if a.count(x)>1]
    odds = [x for x in a if x % 2 == 1]

    if (len(p)>0 and not(len(odds) == 3)) or (not(len(p)>0) and len(odds) == 3):
        c+=1
print(c)
# 1852