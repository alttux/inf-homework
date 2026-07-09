nlst = []
for n in range(1000):
    nb = bin(n)[2:]
    if nb.count('1')%2==0:
        nb = '10.txt' + nb[2:] + '0'
    else:
        nb = '11' + nb[2:] + '1'
    r = int(nb, 2)
    if r>35:
        nlst.append(n)
print(min(nlst))