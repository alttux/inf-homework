for n in range(1, 1000):
    n1 = bin(n)[2:]
    if n % 2 == 0:
        n1 = '1' + n1 + '1'
    else:
        n1 += '10'
    r = int(n1, 2)
    if r > 179:
        print(n)
        break
