res = []
for n in range(1, 10000):
    nb = bin(n)[2:]
    if nb.count('1') % 2 == 0:
        nb = '10' + nb[2:] + '10'
    else:
        nb = '11' + nb[2:] + '01'
    r = int(nb, 2)
    if r > 102:
        print(n)
        break