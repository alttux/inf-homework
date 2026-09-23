def to_a(n, a):
    res = ''
    while n > 0:
        res = str(n%a) + res
        n//=5
    return res


for n in range(50, 101):
    nb = to_a(n, 5)
    if n%5==0:
        nb = nb[:1] + nb + nb[-1:]
    else:
        summa=0
        for i in nb:
            summa+=int(i)
        nb = nb + to_a(summa, 5)

    r = int(nb, 5)

    if  r%5==0:
        print(r)