with open('2.txt') as f:
    count = 0
    for l in f:
        s = sorted(map(int, l.split()))
        p = [x for x in s if s.count(x)>1]
        np = [x for x in s if s.count(x)==1]
        if len(p)==4:
            if sum(p)/len(p) < sum(s)/len(s):
                count += 1

print(count)

# 13
