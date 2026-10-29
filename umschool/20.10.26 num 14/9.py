res = []
for x in range(1, 2031):
    n = 4**230 + 4**130 + 4**30 - x
    c = 0
    while n > 0:
        if n % 4 == 0:
            c += 1
        n //= 4
    if c == 199:
        res.append(x)

print(max(res))