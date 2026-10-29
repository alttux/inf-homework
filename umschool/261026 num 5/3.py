for n in range(1, 255):
    nbo = f'{n:08b}'
    nbo = nbo.replace('1', '|')
    nbo = nbo.replace('0', '1')
    nbo = nbo.replace('|', '0')
    r = str(int(nbo, 2))
    r = int(r[::-1])
    if r == 49:
        print(n)