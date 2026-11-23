def g(s, p, e):
    if s >= 97:
        return p in e
    if p > max(e):
        return False
    mov = [g(s+1, p+1, e), g(s+4, p+1, e), g(s*2, p+1, e)]
    if (p+1) % 2 == e[0] % 2: return any(mov)
    else: return all(mov)

for i in range(1, 96):
    if not(g(i, 0, [1])) and g(i, 0, [2]):
        print(i, end=" ")

print()

for i in range(1, 96):
    if not(g(i, 0, [1])) and g(i, 0, [3]):
        print(i, end=" ")

print()

for i in range(1, 96):
    if not(g(i, 0, [2])) and g(i, 0, [2,4]):
        print(i, end=" ")