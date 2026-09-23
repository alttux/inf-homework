f = open('map4.txt')
c = 0
for l in f:
    s = sorted(list(map(int, l.split())))
    print(s)
    if sum(s)/len(s) < 100:
        c+=1

print(c)