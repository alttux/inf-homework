for n in range(1,1000):
    nb = bin(n)[2:]
    nb += nb[-1]
    if nb.count('1') % 2 == 0: nb += '0'
    else: nb += '1'
    r = int(nb, 2)
    if n > 130:
        print(n)
        break