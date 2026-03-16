lst = {}


def p(n, i):
    s = ''
    while n > 0:
        s = str(n % i) + s
        n = n // i
    return s


for n in range(1, 1000):
    n5 = p(n, 5)
    if n5[-1:] == '0':
        n5 = n5.replace('1', '-')
        n5 = n5.replace('4', '1')
        n5 = n5.replace('-', '4')
        n5 = '33' + n5
    else:
        n5 = n5 + '44'
        n5 = '3' + n5[1:-1] + '2'
    r = int(n5, 5)
    if r < 1922:
        lst[n] = r
vlst = []
for k, v in lst.items():
    vlst.append(v)
klst = []
for k, v in lst.items():
    if v == max(vlst):
        klst.append(k)
print(min(klst))
# 9
