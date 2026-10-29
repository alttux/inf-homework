from math import prod
for n in range(1000,10000):
    s = sum([int(x) for x in str(n)])
    m = max([int(x) for x in str(n)]) + min([int(x) for x in str(n)])
    l = [int(x) for x in str(n)][0]
    r = [int(x) for x in str(n)][-1]
    p1 = s - l
    p2 = m -r
    e = str(max([p1, p2])) + str(min([p1, p2]))

    if e == "129":
        print(n)
