for n in range(1000, 1, -1):
    nb = bin(n)[2:]
    if len(nb) % 2 == 0:
        nb = nb[:len(nb)//2] + '1' + nb[len(nb)//2:]
    r = int(nb, 2)
    if r <= 68:
        print(n)
        break