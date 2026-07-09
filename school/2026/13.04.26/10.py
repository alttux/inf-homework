def treyg(f, R, m):
    return f + R > m and f + m > R and R + m > f

for G in range(1000, 0, -1):
    if all(
        (not treyg(y, 11, 16)) == (not (max(y, 5) > 10))
        and treyg(4, G, y)
        for y in range(1, 10001)
    ):
        print(G)
        break