with open('9.txt') as f:
    c = 0
    for l in f:
        s = sorted(map(int, l.split()))
        p = [x for x in s if s.count(x)>1]
        np = [x for x in s if s.count(x)==1]
        if (p.count(min(s)) == 2 or p.count(min(s)) == 3) and len(set(p))==1:
            if (min(np)**2 + max(np)**2) <= (sum(np)-max(np)-min(np))**2:
                c+=1
print(c)

#752