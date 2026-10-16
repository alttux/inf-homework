def f(n):
    if n == 0:
        return 0
    elif n > 0:
        if n % 3 == 0:
            return f(n-1) + 3 * n
        else:
            return f(n - (n%3)) + 8 * n - 2
    return None

print(f(30))
# 1715
