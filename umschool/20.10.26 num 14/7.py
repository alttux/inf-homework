sp = []
for x in range(1, 3001):
    n = 5**127 + 5**27 - x
    c = 0
    while n > 0:
        if n % 4 == 0:
            c+=1
        n//=4
    sp.append([c, x])

print(sorted(sp)[-5:])