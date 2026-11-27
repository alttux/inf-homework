f = open('9.txt')

c = 0
for l in f:
    s = list(map(int, l.split()))
    p = [x for x in s if s.count(x) > 1]
    np = [x for x in s if s.count(x) == 1]
    if len(p) == 3 and len(np) == 3 and len(set(p)) == 1 and (sum(np)/len(np) < p[0]):
        print(s)
        c+=1

print(c)