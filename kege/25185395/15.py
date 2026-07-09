lm = []
for a1 in range(1000):
    for a2 in range(1000):
        if a1 < a2:
            if all(( (a1 <= x <= a2) or ((22<=x<=40) == (32<=x<=50)) )for x in range(100)):
                lm.append(a2-a1)
print(min(lm))