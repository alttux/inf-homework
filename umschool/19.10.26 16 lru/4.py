from functools import lru_cache


@lru_cache(maxsize=None)
def f(n):
    return 2 * (g(n-2) + 9)

@lru_cache(maxsize=None)
def g(n):
    if n < 20:
        return 2*n
    else:
        return g(n-2) + 3

for i in range(16_000):
    f(i)

print(f(16_888))