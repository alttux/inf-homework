from functools import lru_cache


@lru_cache(None)
def f(n):
    if n >= 2025:
        return n*n
    return f(n+3) + n // 4

for i in range(2500, 0, -1):
    f(i)

print(f(2012) - f(2016))
