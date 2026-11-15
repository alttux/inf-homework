f = open('19.txt')
c = 0

for l in f:
    s = list(map(int, l.split()))
    p = [x for x in s if s.count(x) > 1]
    np = sorted([x for x in s if s.count(x) == 1])

    if len(p) == 3 and len(set(p)) == 1 and (max(np) - min(np))**2 < p[0]**2 :
        c += 1

print(c)
