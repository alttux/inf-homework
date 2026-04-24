c=0
for i in open('9.csv'):
    a = list(map(int, i.split(',')))
    p = [x for x in a if a.count(x) > 1]
    even = [x for x in a if x % 2 == 0]
    odds = [x for x in a if x % 2 == 1]

    if len(p) == 0:
        if len(odds) > len(even):
            if sum(odds) < sum(even):
                c+=1
print(c)
#303