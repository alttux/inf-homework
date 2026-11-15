f = open('15.txt')
c = 0
for l in f:
    s = sorted(map(int, l.split()))
    if (min(s) * 5 < sum(s) - min(s)) and (s[0]*s[1] == s[2]*s[3] or s[0]*s[2] == s[1]*s[3] or s[0]*s[3] == s[1]*s[2]):
        c+=1

print(c)