count = 0
for line in open('9.txt'):
    a = list(map(int, line.split()))
    if len(set(a)) == 6:
        mx, mn = max(a), min(a)
        others = sum(a) - mx - mn
        if (mx + mn) / 2 > others / 4:
            count += 1
print(count)