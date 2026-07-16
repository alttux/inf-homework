f = open('bfd525dd-4a28-47dc-bfa3-59c82c38d7bd_test.txt')
c = 0
for l in f:
    s = sorted(list(map(int, l.split())))

    if (s[2]-s[1])==(s[1]-s[0]):
        print(s)
        c+=1
print(c)