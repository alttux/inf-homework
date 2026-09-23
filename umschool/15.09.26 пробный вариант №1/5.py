rlst = []
for n in range(1, 1000):
    nb = bin(n)[2:]
    if n % 2 == 0:
        nb = '1' + nb + '01'
    else:
        nb = '11' + nb + '1'
    r = int(nb, 2)
    if r > 200:
        print(r)
        rlst.append(r)

print(min(rlst))