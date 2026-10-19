f = open('1.txt')
s = f.readline()
c = 310
ind = []
for i in range(len(s)):
    if s[i] == 'K':
        ind.append(i)

res = []

for i in range(len(ind)-c+1):
    res.append( ind[i+c-1] - ind[i] + 1)

print(min(res))
