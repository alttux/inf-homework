from functools import lru_cache

@lru_cache(None)
def f(n):
    if n == 1:
        return n
    elif n > 1:
        return 2 * n * f(n-1) - 1

for i in range(3000):
    f(i)

print(f(2000)/f(1997))