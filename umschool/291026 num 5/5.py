res = []
for n in range(1, 10000):
    nb = bin(n)[2:]
    if n % 3 == 0:
        nb = nb + nb[-2:]
    else:
        nb = nb + bin((n % 3) * 5)[2:]

    r = int(nb, 2)
    if r >= 156:
        print(n)
        break