c = 0
for l in open('9.txt'):
    r = list(map(int, l.split()))
    if len(set(r)) == 7 and sum(x % 2 == 0 for x in r) > 3:
        c += 1
print(c)