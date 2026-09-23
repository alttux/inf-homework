for n in range(1, 10000):
    nb = bin(n)[2:]
    nbin = nb.replace('0', '-')
    nbin = nbin.replace('1', '0')
    nbin = nbin.replace('-', '1')
    nb = nb + nbin
    r = int(nb, 2)
    if r > 1000:
        print(n)
        break
