from functools import lru_cache


@lru_cache(None)
def F(n):
    if n >= 29:
        return F(n - 7) + 1134
    return 17 * (G(n - 7) - 36)

@lru_cache(None)
def G(n):
    if n >= 27_565:
        return n / 32 + 33
    return G(n + 13) - 1

for n in range(28_000, 0, -1):
    G(n)

print(int(F(676)))