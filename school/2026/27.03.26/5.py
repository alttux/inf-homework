for n in range(128, 256):
    nb = bin(n)[2:]
    nb = nb.replace('0', '-')
    nb = nb.replace('1', '0')
    nb = nb.replace('-', '1')
    nn = int(nb, 2)
    out = n -nn
    if out == 185:
        print(f'исходное: {n}, на выходе: {out}')