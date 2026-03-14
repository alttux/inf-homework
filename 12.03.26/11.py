mx = 0
res = {}
for x in range(57):
    for y in range(57):
        a = 5 * 57 ** 7 + 3 * 57 ** 6 + x * 57 ** 5 + 6 * 57 ** 4 + 6 * 57 ** 3 + \
            y * 57 ** 2 + 3 * 57 ** 1 + 5 * 57 ** 0

        if a % 56 == 0:
            b = y * 57 ** 1 + x * 57 ** 0
            if b ** 0.5 == int(b ** 0.5):
                mx = max(b, mx)
                if not(res.get(mx)):
                    res[mx] = x * 57 ** 1 + y * 57 ** 0
print(res[mx])