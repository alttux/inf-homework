res = []
for n in range(1000, 1, -1):
    nb = bin(n)[2:]
    if nb.count('1') % 2 == 0: nb = '10' + nb[2:] + '0'
    else: nb = '11' + nb[2:] + '11'
    r = int(nb, 2)
    if r < 99:
        print(n)
        break
        