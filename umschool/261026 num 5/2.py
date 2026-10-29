for n in range(1, 255):
    nbo = f'{n:08b}'
    # print(nbo)
    nbo = nbo.replace('1', '|')
    nbo = nbo.replace('0', '1')
    nbo = nbo.replace('|', '0')
    r = int(nbo, 2)**2
    if r == 2601:
        print(n)