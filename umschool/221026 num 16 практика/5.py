from functools import lru_cache

@lru_cache(None)
def f(n):
    if n <= 3:
        return 1
    return (n + 3) * f(n-2)

for i in range(2500):
    f(i)
print(f(2030)/f(2024))