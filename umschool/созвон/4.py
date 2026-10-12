q = range(3, 63)
p = range(38, 90)
a = []

for x in range(1, 1000):
    if ((x in a) or ((x in q) <= (x in p))) == False:
        a.append(x)
c=0
print(a)
print(len(a)==len(set(a)))
print(len(a)/2)
for b in a:
    if b % 2 == 0:
        c+=1

print(c)