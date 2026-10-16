def f(n):
    if n < 4:
        return 4 * n - 1
    else:
        if n % 2 == 0:
            return f(n-2) + 2 * n
        else:
            return f(n-4) + 4 * n + 5

print(f(62))
# 1987