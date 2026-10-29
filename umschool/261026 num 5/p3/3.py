res = []
for n in range(1, 10000):
    nb = bin(n)[2:]
    nb = nb + nb[-1]
    if nb.count('1') % 2 == 0:
        nb = nb + '0'
    else:
        nb = nb + '1'

    r = int(nb, 2)
    if r > 40:
       res.append(r)

print(min(res))
