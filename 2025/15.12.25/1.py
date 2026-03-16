rlst = []


def p(n, i):
    s = ''
    while n > 0:
        s = str(n % i) + s
        n = n // i
    return s


for n in range(1, 1000):
    n3 = p(n, 3)
    if ((n3.count('1') + n3.count('2') * 2) % 9) == 0:
        n3 = n3 + '2'
    else:
        n3 = n3 + p(((n3.count('1') + n3.count('2') * 2) % 9), 3)
    r = int(n3, 3)
    if n > 166:
        rlst.append(r)
print(min(rlst))
# 647
