with open('2.txt') as f:
    count = 0
    for l in f:
        s = sorted(map(int, l.split()))
        p = [x for x in s if s.count(x)>1]
        uc = [x for x in s if x%2==1]
        if (len(p)>0 and not(len(uc)==3)) or (not(len(p)>0) and len(uc)==3):
            count += 1

print(count)

# 1852