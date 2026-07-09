with open('9.txt') as f:
    count = 0
    for l in f:
        s = sorted(map(int, l.split()))
        p = [x for x in s if s.count(x) > 1]
        if (2*(min(s)**2))>(s[1]*s[2]):
            if len(p)>=2:
                count += 1
print(count)
# 56