for n in range(10,10000):
    nb = bin(n)[2:]
    nb = nb + nb[1]
    if nb.count('1') % 2 == 0:
        nb = nb + '00'
    else:
        nb = nb + '10'
    r = int(nb, 2)
    if r > 124:
        print(n)
        break