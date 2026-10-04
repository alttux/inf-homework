import sys
from functools import lru_cache

sys.setrecursionlimit(5000)

@lru_cache(None)
def F(n):
    if n == 1:
        return 1
    return n * F(n - 1)

ans = (F(3238) // 2 + F(3237)) // F(3236)
print(ans)