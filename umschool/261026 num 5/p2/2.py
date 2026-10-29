for n in range(1, 1000):
    nb = bin(n)[2:]
    nb = nb + nb[-1]
    if nb.count('1') % 2 == 0:
        nb = nb + '00'
    else: nb = nb + '10'
    r = int(nb, 2)
    if r >144:
        print(n)
        break
