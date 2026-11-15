f = open('11.txt')
c = 0
for l in f:
    s = sorted(map(int, l.split()))
    if (s[-1]**2 < s[0]*s[1]*s[2]) or ((s[-1]-s[-2]) == (s[-2]-s[-3]) == (s[-3] - s[-4])):
        c+=1

print(c)