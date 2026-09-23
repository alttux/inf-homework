with open('4.txt') as f:
    count = 0
    for l in f:
        s = sorted(map(int, l.split()))
        p = [x for x in s if s.count(x)>1]
        if len(p)==0:
            if 5*(min(s)+max(s)) >= 3*(sum(s)-min(s)-max(s)):
                count += 1

print(count)

# 3333