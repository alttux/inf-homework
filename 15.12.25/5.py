lst = {}


def p(n, i):
    s = ''
    while n > 0:
        s = str(n % i) + s
        n = n // i
    return s


for n in range(1, 1000):
    n7 = p(n, 7)
    if n7[-1:] == '2':
        n7 = n7.replace('1', '-')
        n7 = n7.replace('3', '1')
        n7 = n7.replace('-', '3')
        n7 = '21' + n7
    else:
        n7 = '1' + n7[1:] + '36'
    r = int(n7, 7)
    if r < 744:
        # print(n)
        lst[n] = r
vlst = []
for k, v in lst.items():
    vlst.append(v)
klst = []
for k, v in lst.items():
    if v == max(vlst):
        klst.append(k)

print(min(klst))
# 13
