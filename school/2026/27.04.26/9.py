import sys
sys.setrecursionlimit(10000)
from functools import lru_cache

@lru_cache(maxsize=None)
def F(n):
    if n <= 1:
        return 1
    if n % 2 == 0:
        return 11 * n * F(n - 1)
    else:
        return 10 * F(n - 2)

print(F(2024) // F(2020))  # 100