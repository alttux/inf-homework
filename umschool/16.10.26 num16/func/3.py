def f(n):
    if n  >= 15:
        return n - 2
    else:
        return 4 * f(n+2) - 6

print(f(6))
# 12290