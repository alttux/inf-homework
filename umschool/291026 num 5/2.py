res = []
for n in range(1, 10000):
    nb = bin(n)[2:]
    if n % 2 == 0:
        nb = nb + nb[:2]
    else:
        nb = '1' + nb + '0'
    r = int(nb, 2)
    if r > 7318:
        res.append(r)

print(min(res))