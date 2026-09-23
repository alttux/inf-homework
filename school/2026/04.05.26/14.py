res = []
for x in range(1, 4001):
    s = ''
    n = 5**17 + 5**12 - x
    while n > 0:
        s += str(n % 5)
        n //= 5
    res.append((s.count('0'), x))

print(max(res, key=lambda x: (x[0], -x[1])))

# 3125