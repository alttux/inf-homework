for n in range(1, 10000):
    nb = bin(n)[2:]
    s1 = nb.count('1') % 2
    nb += str(s1)
    s2 = nb.count('1') % 2
    nb += str(s2)
    r = int(nb, 2)
    if r > 85:
        print(n)
        break
