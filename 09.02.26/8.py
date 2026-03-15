with open('8.txt') as f:
    count = 0
    for l in f:
        s = sorted(map(int, l.split()))
        p = [x for x in s if s.count(x) > 1]
        if (len(p)==0 and not(max(s)>(sum(s)-max(s)))) or (not(len(p)==0) and (max(s)>(sum(s)-max(s)))):
                count += 1
print(count)
# 2222