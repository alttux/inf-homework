def f(n):
    if n <= 3:
        return n**3
    elif n > 3 and n % 2 == 0:
        return n + 2 + 8 * f(n - 2)
    elif n > 3 and n % 2 != 0:
        return 17*n + f(n - 3) - f(n - 4) + 8
    
c=0
for i in range(134, 928):
    if f(i) % 6 == 0:
        c+=1

print(c)