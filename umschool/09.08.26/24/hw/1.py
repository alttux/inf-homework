f = open('1.txt')
l = f.readline()
ltrs = {}.fromkeys(set(l), 0)
for i in range(len(l)-1):
    l1, l2 = l[i: i+2]
    if l2 == 'Z':
        ltrs[l1]+=1
print(ltrs)
print(sorted(ltrs, key=ltrs.get))