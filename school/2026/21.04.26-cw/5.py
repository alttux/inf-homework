for n in range(1000):
    nb = bin(n)[2:]
    s = nb + str(nb.count('1')%2)
    s = s + str(s.count('1')%2)
    r = int(s, 2)
    if r > 253:
        print(n)
        break
