lst = {}
def p(n, i):
    s = ''
    while n > 0:
        s = str(n % i) + s
        n = n // i
    return s


for n in range(1, 1000):
    n4 = p(n, 4)
    if n4[0] == "3":
        n4 = n4.replace('1', '-')
        n4 = n4.replace('3', '1')
        n4 = n4.replace('-', '3')
        n4 = '21' + n4
    else:
        n4 += '11'
        n4 = '2' + n4[1:]
    r = int(n4, 4)
    if r < 598:
        print(n)
        lst[n] = r
vlst = []
for k, v in lst.items():
    vlst.append(v)
klst = []
for k, v in lst.items():
    if v == max(vlst):
        klst.append(k)

print(max(klst))

# 63