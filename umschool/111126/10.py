f = open('10.txt')
c = 0
for l in f:
    s = sorted(map(int, l.split()))
    if s[0] + s[1] > s[2]:
        c+=1

print(c)