for n in range(1, 10000):
    nb = bin(n)[2:]
    if nb.count('1') % 2 == 0:
        nb = '11'+ nb[2:] + '1'
    else:
        nb = '10' + nb[2:] + '0'
    r = int(nb, 2)
    # print(r)
    if r > 150:
        print(n)
        break
