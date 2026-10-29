for n in range(1, 10000):
    nb = bin(n)[2:]
    nb = nb.replace('0', '2')
    nb = nb.replace('1', '0')
    nb = nb.replace('2', '1')
    r = n - int(nb, 2)
    if r == 817:
        print(n)
        break