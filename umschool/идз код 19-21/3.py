def g(x, s, p, e):
    if (x + s) >= 97:
        return p in e
    if (x+s) < 97 and p == max(e):
        return False
    mov = [g(x+3, s, p+1, e), g(x*2, s, p+1, e), g(x, s+3, p+1, e), g(x, s*2, p+1, e) ]
    if (p+1) % 2 == (e[0] % 2):
        return any(mov)
    else:
        return all(mov)

for i in range(1, 86):
    if  g(11, i, 0, [2]):
        print(i, end=" ")

print()

for i in range(1, 86):
    if not(g(11, i, 0, [1])) and g(11, i, 0, [3]):
        print(i, end=" ")

print()

for l in range(1, 86):
    if not(g(11, l, 0, [2])) and g(11, l, 0, [2, 4]):
        print(l, end=" ")
