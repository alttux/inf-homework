res = []
for n in range(1, 1000):
    nb = bin(n)[2:]
    if n % 2 == 0:
        nb = nb + '01'
    else: nb = nb + '10'
    r = int(nb, 2)
    if r > 146:
        res.append(r)

print(min(res))