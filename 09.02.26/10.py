with open('10.txt') as f:
    count = 0
    for l in f:
        s = sorted(map(int, l.split()))
        p = [x for x in s if s.count(x) > 1]
        if len(p)==0:
            if sum(s)%3==0:
                count += 1
print(count)
# 610