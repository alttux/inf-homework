f = open('42db3dfe-0e67-4a29-bd90-a27ab0f65793_test.txt')
c = 0
for l in f:
    s = sorted(list(map(int, l.split())))

    if ((s[0]%3)+(s[1]%3)+(s[2]%3))==5:
        print(s)
        c+=1
print(c)