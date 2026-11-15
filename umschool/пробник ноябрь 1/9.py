f = open('9.txt')
c = 0

for l in f:
    s = list(map(int, l.split()))
    if (len(s) == len(set(s))) and ((2*sum([max(s), min(s)])) < (sum(s) - max(s) - min(s))):
        c += 1

print(c)