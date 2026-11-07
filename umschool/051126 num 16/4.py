from functools import cache

@cache
def f(n):
    if n < 11:
        return 8
    return (n+1) * f(n-5)

for i in range(1, 250_000, 5):
    f(i)

print((f(246_911)//8 + 11_111*f(246_906)) / f(246_901))
