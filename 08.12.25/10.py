for n in range(1, 1000):
    n1 = bin(n)[2:]
    n1 += '0' if n1.count('1') % 2 == 0 else '1'
    n1 += '0' if n1.count('1') % 2 == 0 else '1'

    r = int(n1, 2)

    if r > 204:
        print(r)
        break
