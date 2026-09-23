for n in range(1, 1000):
    nb = bin(n)[2:]
    if n % 3 == 0:
        nb = nb + nb[-3:]
    else:
        nb = nb + bin((n%3)*3)[2:]
    r = int(nb, 2)
    if 110 < r < 140:
        print(n, r)


