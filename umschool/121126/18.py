f = open('18.txt')
c = 0

for l in f:
    s = list(map(int, l.split()))
    p = [x for x in s if s.count(x) > 1]
    np = sorted([x for x in s if s.count(x) == 1])

    if len(p) == 2 and len(set(p)) == 1 and p[0]**2 > np[-1] * np[-2]:
        c += 1

print(c)
