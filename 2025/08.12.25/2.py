for n in range(1, 1000):
    n1 = bin(n)[2:]
    n1 += str(n1.count('1') % 2)
    n1 += str(n1.count('1') % 2)
    r = int(n1, 2)
    if r > 253:
        print(n)
        break
