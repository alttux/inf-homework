def to_n(x, n):
    s = ''
    while x > 0:
        s = str(x%n)+s
        x = x//n
    return s
nulls = []
for x in range(0, 8410):
    a = 29**293 + 29**271 - x
    a_29 = to_n(a, 29)
    nulls.append(a_29.count('0'))
print(max(nulls))
#292