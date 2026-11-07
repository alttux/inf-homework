from functools import cache

@cache
def f(n):
    if n == 1:
        return 1
    elif n > 1:
        return n * f(n - 1)
    return None

for i in range(1, 3000):
    f(i)

print((f(3038) + 5 * f(3037)) / f(3036))

