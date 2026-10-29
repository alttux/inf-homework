res = []
for n in range(1, 10000):
    nb = bin(n)[2:]
    nb = nb + str(nb.count('1') % 2)
    nb = nb + str(nb.count('1') % 2)
    r = int(nb, 2)
    if r > 1096:
        print(n)
        break