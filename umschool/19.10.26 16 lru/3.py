from functools import lru_cache


@lru_cache(None)
def f(n):
    if n >= 3000:
        return n
    else:
        return n + 5 + f(n+2)

for i in range(3000, 0, -1):
    f(i)
    
print(f(108) - f(112))

