from functools import lru_cache
@lru_cache(maxsize=None)
def f(n):
    if n <= 10:
        return n
    return (n+2) * f(n-2)
for i in range(10, 100000):
    f(i)

print((f(12748) - f(19563)) // f( 19562) + 1234)