lst = {}


def p(n, i):
    s = ''
    while n > 0:
        s = str(n % i) + s
        n = n // i
    return s


for n in range(1, 1000):
    n4 = p(n, 3)
    if (n4.count('1') + n4.count('2') * 2) % 4 == 0:
        n4 = n4.replace('1', '-')
        n4 = n4.replace('2', '1')
        n4 = n4.replace('-', '2')
        n4 = '10.txt' + n4
    else:
        n4 += '20'
        n4 = n4[0] + '0' + '2' + n4[3:]

    r = int(n4, 3)
    if r > 302:
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

# 51
