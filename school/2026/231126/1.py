def t34(n, m):
    if n < m: return 0
    elif n == m: return 1
    nc = (n//3)*3 if n % 3 != 0 else n//3
    return  t34(n-5, m) + t34(nc, m)

print(t34(103, 73)*t34(73, 24))