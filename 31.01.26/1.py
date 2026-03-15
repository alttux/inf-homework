with open('1.txt') as f:
    count = 0

    for l in f:
        s = sorted(map(int, l.split()))
        p = [x for x in s if s.count(x) > 1]
        np = [x for x in s if s.count(x) == 1]
        if len(set(p)) == 1 and len(p)==2:
            if sum(np) / len(np) <= p[0]:
                count += 1
print(count)


# 2241