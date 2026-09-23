def F(n):
    if n < 2:
        return 1
    if n >= 2 and n % 5 == 0:
        return F(n / 5) - 1
    if n >= 2 and n % 5 != 0:
        return F(n - 1) + 5


fs = []
for n in range(100, 200):
    fs.append(F(n))

print(min(fs))
