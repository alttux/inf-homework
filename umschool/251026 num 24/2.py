f = open('2.txt')
c = 0
res = []
for l in f:
    if l.count('a') < 20:
        for s in l:
            res.append(l.rindex(s) - l.index(s))
print(max(res))