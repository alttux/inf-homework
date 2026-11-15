f = open('21.txt')
c = 0

for l in f:
    s = list(map(int, l.split()))
    p = [x for x in s if s.count(x) > 1]
    np = sorted([x for x in s if s.count(x) == 1])

    if len(p) == 5 and len(set(p)) == 2 and (p.count(list(set(p))[0]) == 3 or p.count(list(set(p))[0]) == 2) and (p.count(list(set(p))[1]) == 3 or p.count(list(set(p))[1]) == 2) and sum(p) > 3 * sum(np) :
        print(sum(s))

print(c)
