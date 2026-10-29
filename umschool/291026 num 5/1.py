for n in range(1, 1000):
    nb = bin(n)[2:]
    if n % 2 != 0:
        nb = '10' + nb
    else:
        nb = '1' + nb + '10'
    r = int(nb, 2)
    if r > 697:
        print(n)
        break