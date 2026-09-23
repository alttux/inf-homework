def delit(n, m):
    return n % m == 0

B = range(96, 129)

for A in range(1, 1000):
    if all((delit(x, A) or (not(x in B) or not(delit(x, 26)))) for x in range(1, 2000)):
        print(A)