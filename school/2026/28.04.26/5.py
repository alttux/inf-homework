for n in range(1000):
    nb = bin(n)[2:]
    if n%5==0:
        nb = nb + '11'
    else:
        nb = nb + bin(n//5)[2:]
    r = int(nb, 2)
    if r >= 783 and n%2!=0:
        print(n)
        break