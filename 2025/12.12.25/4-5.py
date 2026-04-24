nlst = []
for n in range(1000):
    nb = bin(n)[2:]
    if n%2==0:
        nb = '10.txt'+ nb
    else:
        nb = '1'+ nb + '01'
    r = int(nb, 2)
    if r>541:
        nlst.append(n)
print(min(nlst))