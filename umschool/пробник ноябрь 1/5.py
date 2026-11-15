res = []
for n in range(1, 100000):
    nb = bin(n)[2:]
    if n % 2 == 0:
        nb = '11' + nb + '0'
    else:
        nb = '1' + nb + '01'
    r = int(nb, 2)
    if r > 140:
       res.append(r)

print(min(res))
