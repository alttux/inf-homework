c = 0
for G in range(1, 1001):
    if all(
            ((f<6) <= (f**2 <G)) and (h**2 <= G) <= (h<=6)
            for h in range(1, 300)
            for f in range(1, 300)
    ):
        c+=1
print(c)