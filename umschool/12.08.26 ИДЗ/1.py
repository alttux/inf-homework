for n in range(0, 256):
    nb = bin(n)[2:]
    # print(nb)
    nb = nb.replace('0', '*')
    nb = nb.replace('1', '0')
    nb = nb.replace('*', '1')
    # print(nb)

    nbt = str(int(nb, 2))
    r = int(nbt[::-1])
    if r == 97:
        print(n)