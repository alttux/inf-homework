for n in range(700, 100000):
    nb = bin(n)[2:]
    nb = nb[::-1]
    r = int(nb, 2)
    if r == 87:
        print(n, r)