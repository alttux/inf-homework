lst = {}
def p(n, i):
    s = ''
    while n > 0:
        s = str(n % i) + s
        n = n // i
    return s


for n in range(1, 1000):
    n4 = p(n, 4)
    if (n4.count('1')+n4.count('2')*2+n4.count('3')*3) == "3":
        n4 = n4.replace('0', '-')
        n4 = n4.replace('2', '0')
        n4 = n4.replace('-', '2')
        n4 = '32' + n4
    else:
        n4+='33'
        n4 = n4[0] + '1' + '0' + n4[3:]
    r = int(n4, 4)
    if r > 320:
        print(n)
        lst[n] = r
vlst = []
for k, v in lst.items():
    vlst.append(v)
klst = []
for k, v in lst.items():
    if v == min(vlst):
        klst.append(k)

print(max(klst))

# 31