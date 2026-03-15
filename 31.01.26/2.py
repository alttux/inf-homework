with open('2.txt') as f:
    count = 0

    for l in f:
        s = sorted(map(int, l.split()))
        p = [x for x in s if s.count(x) > 1]
        np = [x for x in s if s.count(x) == 1]
        if len(p) == 3:
            if (p[0]+p[1]+p[2])**2 > (np[0]+np[1]+np[2])**2:
                count += 1
print(count)


# 273