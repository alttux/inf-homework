for n in range(1, 255):
    nbo = f'{n:08b}'
    nbo = nbo.replace('1', '|')
    nbo = nbo.replace('0', '1')
    nbo = nbo.replace('|', '0')
    r = int(nbo, 2) - n
    if r == -9:
        print(n)
