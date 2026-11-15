f = open('num 8_9')
c = 0
for l in f:
    s = list(map(int, l.split()))
    if len(set(s)) == 2 and s.count(list(set(s))[0]) == 2:
        c+=1

print(c)