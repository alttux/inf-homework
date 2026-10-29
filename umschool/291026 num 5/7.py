def troi(n):
    s = ''
    while n > 0:
        s = str(n%3) + s
        n//=3
    return s
res = []
for n in range(1, 1000):
    nt = troi(n)
    if n % 3 ==0:
        nt += nt[:2]
    else:
        nt = troi((n%3)*5)

    r = int(nt, 3)
    if r > 533:
        res.append(r)

print(min(res))