def g(s, p, e):
    if s >= 70:
        return p in e
    if p > max(e):
        return False
    mov = [g(s+2, p+1, e), g(s*3, p+1, e)]
    if (p+1) % 2 == e[0] % 2:
        return any(mov)
    else:
        return any(mov)

for i in range(1, 70):
    if not(g(i, 0, [1])) and g(i, 0, [2]):
        print(i, end=" ")

