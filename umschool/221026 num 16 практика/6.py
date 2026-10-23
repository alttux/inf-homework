from functools import lru_cache


@lru_cache(None)
def f(n):
    if n < 10:
        return 3
    return (n+4) * f(n-5)

for i in range(7, 260_000, 5):
    f(i)

print((f(257_482)//603 - 427 * f(257_477))//f(257_472))
