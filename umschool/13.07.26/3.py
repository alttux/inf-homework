f = open('map3.txt')
c = 0
for l in f:
    s = sorted(list(map(int, l.split())))
    print(s)
    if s[2] < s[1]+s[0]:
        c+=1

print(c)