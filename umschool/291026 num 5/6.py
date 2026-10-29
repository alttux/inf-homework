res = []
for n in range(10, 10000):
    nb = bin(n)[2:]
    if n % 3== 0:
        nb += nb[-3]
    else:
        nb += bin((n % 3)*3)[2:]
    r = int(nb, 2)
    if 120 < r < 130:
        print(n, r)
        break