from itertools import permutations
c=0

for i in open('9_3.csv'):
    a = sorted(map(int, i.split(',')))
    if a[-2]**2 > a[0]*a[-1]:
        for j in permutations('0123', 4):
            if a[int(j[0])]*a[int(j[1])]==a[int(j[2])]*a[int(j[3])]:
                c+=1
                break
print(c)
13