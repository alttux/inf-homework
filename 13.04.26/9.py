def treyg(f, R, m):
    return f + R > m and f + m > R and R + m > f

def maks(a, b):
    return max(a, b)

for G in range(1000, 0, -1):
    if all(
        (treyg(y, 10, 20) <= (not (maks(y, 8) > 24)))
        ==
        (not treyg(3, G, y))
        for y in range(1, 10001)
    ):
        print(G)
        break
