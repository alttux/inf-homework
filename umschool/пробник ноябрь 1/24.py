f = open('57707297-45b3-4efe-8b38-d8e90298cf80_24.txt')
s = f.readline()
# s = 'aaaaaaaCABaaaaaaaaaCABaaaCABaaaaCABaa'
ind_CAB = []

for i in range(len(s)):
    if s[i:i+3] == 'CAB':
        ind_CAB.append(i)
res = []
print(ind_CAB)
for i in range(len(ind_CAB)-90+1):
    r = ind_CAB[i+90-1]+3-ind_CAB[i]
    res.append(r)

print(res)
print(min(res))