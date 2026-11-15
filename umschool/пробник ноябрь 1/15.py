b = range(17, 59)
c = range(34, 92)
res = []
for a1 in range(-100, 100):
    for a2 in range(a1, 100):
        if all((x in range(a1, a2+1)) or ((x in b) == (x in c)) for x in range(1, 200)):
            print(a1, a2)
            res.append(a2-a1)

print(min(res))
