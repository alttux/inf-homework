res = []
for n in range(1, 1000):
    nb = bin(n)[2:]
    nb +=nb[-1]
    if nb.count('1') % 2 ==0:
        nb += '00'
    else:
        nb += '11'

    r = int(nb, 2)
    if r > 177:
        print(n)
        break