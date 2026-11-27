def delo(n, m):
    return n % m == 0

b = range(115, 151)
for a in range(1, 1000):
    if all(delo(x, a) or ((x in b) <= (not delo(x, 37))) for x in range(1,1000)):
        print(a)