nlst = []
for n in range(1000):
    nb = bin(n)[2:]
    if n%2==0:
        nb = nb + '00'
    else:
        nb = nb + '11'
    r = int(nb, 2)
    if r>215:
        nlst.append(n)
print(min(nlst))