from functools import lru_cache


@lru_cache
def f(n):
    if n == 1:
        return 1
    elif n > 1:
        return (2 * n -2) * f(n-1)

for i in range(3000):
    f(i)

print(f(3029) // f(3027))