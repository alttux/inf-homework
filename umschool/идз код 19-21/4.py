def g(x, s, p, e):
    if (x + s) >= 117:
        return p in e
    if p == max(e) and (x + s) < 117:
        return False
    mov = [g(x+2, s, p+1, e), g(x*3, s, p+1, e), g(x, s+2, p+1, e), g(x, s*3, p+1, e)]
    if (p+1) % 2 == (e[0] % 2):
        return any(mov)
    else:
        return all(mov)

for i in range(1, 110):
    if not(g(7, i, 0, [2])) and g(7, i, 0, [2, 4]):

        print(i, end=" ")

print()

