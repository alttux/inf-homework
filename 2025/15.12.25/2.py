lst = {}

for n in range(1, 1000):
    n8 = oct(n) [2:]
    if n8[0]==5:
        n8 = n8.replace('2', '-')
        n8 = n8.replace('1', '2')
        n8 = n8.replace('-', '1')
        n8 = '11'  + n8
    else:
        n8 = n8 + '10.txt'
        n8 = '2' + n8[1:-1] + '0'
    r = int(n8, 8)
    if r<1354:
        lst[n] = r
vlst = []
for k, v in lst.items():
    vlst.append(v)
klst = []
for k, v in lst.items():
    if v == max(vlst):
        klst.append(k)

print(max(klst))

# 61