def F(n):
    if n < 2:
        return 1
    if n >= 2 and n % 4 == 0:
        return F(n / 4) - 1
    if n >= 2 and n % 4 != 0:
        return F(n - 1) + 1


fs = []
for n in range(100, 201):
    fs.append(F(n))

print(max(fs))
