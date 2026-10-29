for n in range(10,10000):
    nb = bin(n)[2:]
    nb = nb + str(nb.count('1') % 2)
    nb = nb + str(nb.count('1') % 2)
    r = int(nb, 2)
    if r > 630:
        print(n)
        break