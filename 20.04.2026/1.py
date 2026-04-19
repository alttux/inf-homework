c = 0
for G in range(1, 1001):
    if all(
            ((f < G) <= (f ** 2 < 81)) and ((h ** 2 <= 36) <= (h <= G))
            for f in range(1, 300)
            for h in range(1, 300)
    ):
        c+=1
print(c)