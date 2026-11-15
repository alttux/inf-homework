f = open('17.txt')
c = 0

for l in f:
    s = sorted(list(map(int, l.split())))
    p = [x for x in s if s.count(x) == 3]
    np = [x for x in s if s.count(x) == 1]
    if len(set(p)) == 1 and len(p) == 3 and len(np) == 4 and sum(np)/len(np) <= p[0]:
        print(sum(s))

# print(c)