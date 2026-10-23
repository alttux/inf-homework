from functools import lru_cache


def f(n):
    return 3 * g(n-4) + 7

@lru_cache(None)
def g(n):
    if n < 15:
        return 4 * n
    return g(n-3)+5

for i in range(19_000):
    f(i)

print(f(18_004))