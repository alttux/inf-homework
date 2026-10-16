res = []
for x in range(1, 2026):
    s = 6**210 + 6**180 - x
    c = 0
    while s > 0:
        if s % 6 == 0:
            c+=1
        s//=6
    res.append([c, x])

print(max(res))
print(sorted(res)[-5:])