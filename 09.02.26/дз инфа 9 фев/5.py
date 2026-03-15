for i in open('9_5.csv'):
    a = sorted(map(int, i.split(',')))
    p = [x for x in a if a.count(x)>1]
    c=set(p)
    if len(set(p))==2 and len(p) == 6:
        if p.count(list(c)[0]) == p.count(list(c)[1]):
            if a[0] not in p:
                print(sum(a))
                break
318