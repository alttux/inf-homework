f = open('2.txt')
l = f.readline()
ltrs = {}.fromkeys(set(l), 0)
for i in range(len(l)-2):
    l1, l2, l3 = l[i: i+3]
    if l1 == "D" and l3 == "P":
        ltrs[l2]+=1
print(ltrs)
print(sorted(ltrs, key=ltrs.get))
