for n in range(1, 1000):
    n1 = bin(n)[2:]
    if n % 2 == 0:
        n1 = '10' + n1
    else:
        n1 = '1' + n1 + '01'
    r = int(n1, 2)
    if r < 30:
        print(n)
