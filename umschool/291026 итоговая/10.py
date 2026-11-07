res = []
for n in range(1, 1000):
    nb = bin(n)[2:]
    nb += str(nb.count('1')%2)
    nb += str(nb.count('1') % 2)
    r = int(nb, 2)
    if r > 680:
        res.append(r)

print(min(res)
      )