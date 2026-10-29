def troi(n):
    s = ''
    while n > 0:
        s = str(n%4) + s
        n//=4
    return s
res = []
for n in range(1, 1000):
    nt = troi(n)
    if n % 2 ==0:
        nt += '13'
    else:
        nt = '1' + nt + troi((n%3))

    r = int(nt, 4)
    if r > 320:
        print(n)
        break
