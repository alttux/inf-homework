f = open('task1.txt')
s = f.readline()
c = 210

ind_t = []
for i in range(len(s)):
    if s[i] == 'T':
        ind_t.append(i)
res = []
for i in range(len(ind_t)-c+1):
    res.append(ind_t[i+c-1]-ind_t[i] + 1)

print(min(res))
