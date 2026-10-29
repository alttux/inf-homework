from functools import lru_cache

@lru_cache(maxsize=None)
def F(n):
    if n == 0:
        return 1
    return F(n // 2) + F(n // 3)

print(F(10**18))