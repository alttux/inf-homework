def to21(n):
    s = ''
    while n > 0:
        s = str(n%21)+s
        n//=21
    return s

a = 5 * 21 ** 2026 + 3 * 21 ** 1518 - 4 * 21 ** 760 + 2 * 21 ** 94 - 1985
print(to21(a).count('0'))