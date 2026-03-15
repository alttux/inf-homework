from itertools import permutations
c=0

for i in open('9_6.csv'):
    a = sorted(map(int, i.split(',')))
    if (a[0]+a[-1])% 3 == 0:
        for j in permutations('0123', 4):
            if a[int(j[0])]-a[int(j[1])]==a[int(j[2])]-a[int(j[3])]:
                c+=1
                break
print(c)
6