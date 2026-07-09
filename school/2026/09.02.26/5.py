with open('5.txt') as f:
    count = 0
    for l in f:
        s = sorted(map(int, l.split()))
        p = [x for x in s if s.count(x) > 1]
        if len(p)==6 and  len(set(p))==2:
            if s.count(min(s))==1:
                print(sum(s))
                break

# 318