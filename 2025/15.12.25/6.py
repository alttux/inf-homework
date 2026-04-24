lst = {}


def p(n, i):
    s = ''
    while n > 0:
        s = str(n % i) + s
        n = n // i
    return s


for n in range(1, 1000):
    n4 = p(n, 6)
    if n4[0] == "3":
        n4 = n4.replace('2', '-')
        n4 = n4.replace('0', '2')
        n4 = n4.replace('-', '0')
        n4 = '10.txt' + n4
    else:
        n4 = '5' + n4[1:] + '13'
    r = int(n4, 6)
    if r < 1299:
        print(n)
        lst[n] = r
vlst = []
for k, v in lst.items():
    vlst.append(v)
klst = []
for k, v in lst.items():
    if v == max(vlst):
        klst.append(k)

print(min(klst))
# 11
