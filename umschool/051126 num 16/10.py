from functools import cache

@cache
def f(n):
    if n > 11:
        return n * n * n + 5
    elif n <= 11 and n % 2 == 0:
        return 5 * f(n+2) + f(n+1)
    elif n <= 11 and n % 2 != 0:
        return f(n+3) + f(n+2)

c = 0
for i in range(1, 401):
    if str(f(i)).count('7') == 0:
        c+=1

print(c)